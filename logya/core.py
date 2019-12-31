# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import datetime

from collections import namedtuple
from operator import itemgetter

from logya import path
from logya import config
from logya.docreader import DocReader
from logya.template import Template
from logya.writer import write


Collection = namedtuple('Collection', ['docs', 'template', 'urls'])


def get_collection_var(url, collection_index):
    """Get collections var from site.yaml if url is in a subdirectory of the
    paths defined in collections."""

    parent_path = '/'.join(path.parent_dirs(url))
    return collection_index.get(parent_path)


class Logya(object):
    """Main logic for creating, building and serving a static site."""

    index_filename = 'index.html'

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        self.verbose = kwargs.get('verbose', False)

        # dir_site is an optional argument of the generate command, which may
        # instantiate the class with a value of None for dir_site.
        dir_site = kwargs.get('dir_site')
        self.dir_site = dir_site if dir_site else os.getcwd()

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        cwd = self.dir_site
        self.dir_content = path.join(cwd, 'content', required=True)
        self.config = config.load(path.join(cwd, 'site.yaml', required=True))

        self.dir_templates = path.join(cwd, 'templates', required=True)
        self.template = Template(self)

        self.dir_bin = path.join(cwd, 'bin')

        # Make all settings in site section available to templates.
        self.template.vars.update(self.config['site'])

        # Optional directory with static files like css, js and images.
        self.dir_static = path.join(cwd, 'static')

        # Directory is created by the generate command.
        self.dir_deploy = path.join(cwd, 'deploy')

        self.base_url = self.config['site'].get('base_url')
        # base_url must be defined in settings
        if not self.base_url:
            raise Exception('base_url not set in site config.')

        # A dictionary of parsed documents indexed by resource paths.
        self.docs = {}

        # A dictionary of document collections.
        self.index = {}

        # A dictionary of collection names and distinct values.
        self.collections = {}

        # Set default templates once for a Logya instance.
        self.templates = {
            'doc': self.config['content']['doc']['template'],
            'index': self.config['content']['index']['template'],
            'rss': self.config['content']['rss']['template']
        }

        self.pages = {}
        # Set default pages for templates.
        for ctype, template in self.templates.items():
            self.pages[ctype] = self.template.env.get_template(template)

        # Set languages if specified.
        if 'languages' in self.config:
            self.languages = self.config['languages']

        # Map collection paths to config variables (vars) to make collection
        # settings accessible via index URLs.
        self.collection_index = {
            v['path']: k for k, v in self.config['collections'].items()}

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)

    def get_doc_template(self, doc):
        """Get template setting from doc otherwise from configuration."""

        return doc.get('template', self.templates['doc'])

    def get_index_template(self, fullpath):
        """Get template file name for given fullpath.

        If a collection is set in site.yaml for fullpath, use the corresponding
        template if set. Otherwise return the default index template.
        """

        template = self.templates['index']
        attr = get_collection_var(fullpath, self.collection_index)

        # Remove top-level language directory from fullpath if inside that language, so the definitions in site.yaml can be matched.
        if not attr and getattr(self, 'languages', None):
            for lang in self.languages:
                prefix = lang['code'] + '/'
                if fullpath.startswith(prefix):
                    attr = get_collection_var(fullpath[len(prefix):], self.collection_index)
                    break
        if attr:
            template = self.config['collections'][attr].get('template', template)
        return template

    def _update_index(self, doc, url=None):
        """Add a doc to index determined from given url.

        For each directory in the URL except for the one containing the content
        file itself a collection is created, if it doesn't exist, and the
        document is added to it.
        """

        if url is None:
            url = doc['url']

        dirs = path.parent_dirs(url)
        for fullpath in path.parent_paths(dirs):
            if fullpath not in self.index:
                template = self.get_index_template(fullpath)
                self.index[fullpath] = Collection(docs=[], template=template, urls=set())

            # Don't add documents more than once to a collection. Important to
            # check and add doc['url'], because url can be an index url like tags.
            if doc['url'] not in self.index[fullpath].urls:
                self.index[fullpath].urls.add(doc['url'])
                self.index[fullpath].docs.append(doc)

    def _update_doc_index(self, doc, attr, basepath):
        """Add the doc to the index defined for the attribute."""

        for val in doc[attr]:
            url = '/{}/{}/'.format(basepath, path.slugify(val))

            links = attr + '_links'
            doc[links] = doc.get(links, []) + [(url, val)]

            # Must append file name to url to create subdir.
            self._update_index(doc, url + self.index_filename)

    def update_index(self, doc):
        """Add document to index based on index headers."""

        # Don't index documents with noindex set to a true value.
        if doc.get('noindex'):
            return

        self._update_index(doc)

        # Add to special __index__ for RSS generation.
        self._update_index(doc, '__index__/index/')

        for attr, collection in self.config['collections'].items():
            if attr not in doc:
                continue
            self._update_doc_index(doc, attr, collection['path'])
            self.collections[attr] = self.collections.get(attr, []) + list(filter(None, doc[attr]))

            # Optionally create language specific indexes.
            if not getattr(self, 'languages', None):
                continue
            for lang in self.languages:
                if lang['code'] == doc['url'].split('/')[1]:
                    # Make document language available to templates if not already specified.
                    if 'language' not in doc:
                        doc['language'] = lang['code']
                    self._update_doc_index(doc, attr, '{}/{}'.format(lang['code'], collection['path']))

    def build_index(self, mode=None):
        """Build index of documents for content directories to be created.

        The mode argument hints the Logya command that was executed."""

        msg_duplicate = 'The URL {} is already used and will be overwritten.'

        for doc in DocReader(self.dir_content).parsed:
            url = doc['url']
            # Warn user about duplicate URLs when not in serve mode.
            if 'serve' != mode and url in self.docs:
                print(msg_duplicate.format(url))
            self.docs[url] = doc
            self.update_index(doc)

        # For each collection sort docs by creation dates in descending order.
        for url, collection in self.index.items():
            collection.docs.sort(key=itemgetter('created'), reverse=True)

        # Make index available to templates.
        self.template.vars['index'] = self.index

        # Make collections values unique and turn list of attribute values into path, value tuples.
        for coll_path, name in self.collection_index.items():
            values = []
            for val in sorted(set(self.collections.get(name, []))):
                url = '/{}/{}/'.format(coll_path, path.slugify(val))
                values.append((url, val))
            if values:
                self.collections[name] = values

        # Make collections available to templates.
        self.template.vars['collections'] = self.collections

    def index_title(self, s):
        """Title for index pages, usually created from directory paths."""

        return ' » '.join(s.split('/')).replace('-', ' ').title()

    def write_rss(self, feed_title, url, docs):
        """Write RSS 2.0 XML file in target directory"""

        self.template.vars['url'] = self.base_url
        self.template.vars['title'] = feed_title
        self.template.vars['description'] = feed_title
        self.template.vars['last_build'] = datetime.datetime.now()
        self.template.vars['docs'] = docs

        content = self.pages['rss'].render(self.template.vars)

        filename = path.target_file(
            self.dir_deploy, path.join(url, 'rss.xml'))
        write(filename, content)

    def write_index(self, url, collection):
        """Write an auto-generated index.html file."""

        check_doc_url = '/{}'.format(path.join(url, self.index_filename))
        # make sure there exists no document at the index url
        if check_doc_url not in self.docs:
            # Ugly fix for issue #32: delete description var. This is called
            # for every index, instead of once for all, because write_index is
            # called in serve mode. Also there may remain other vars causing
            # future problems.
            # Emptying the vars dict does not work either, because the index
            # key is set in build_index and needed.
            if 'description' in self.template.vars:
                del self.template.vars['description']

            title = self.index_title(url)

            self.template.vars['docs'] = collection.docs
            self.template.vars['title'] = title
            self.template.vars['canonical'] = '{:s}/{:s}/'.format(self.base_url, url)

            page = self.template.env.get_template(collection.template)
            content = page.render(self.template.vars)

            filename = path.target_file(self.dir_deploy, url)
            write(filename, content)

            # write directory RSS file
            self.write_rss(title, url, collection.docs)

    def write_index_files(self):
        """Write index.html files to deploy directories where non exists.

        If no template is specified in configuration index won't be written.
        """

        feed_title = self.config['site'].get('feed_title', 'RSS Feed')

        for url, collection in self.index.items():
            if '__index__' != url:
                self.write_index(url, collection)

        # write root RSS file
        if '__index__' in self.index:
            self.write_rss(feed_title, '', self.index['__index__'].docs)
