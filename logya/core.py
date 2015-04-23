# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import datetime

from operator import itemgetter

from logya import path
from logya.compat import execfile
from logya.config import Config
from logya.docreader import DocReader
from logya.template import Template
from logya.writer import FileWriter


class Logya(object):
    """Main logic for creating, building and serving a static site."""

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        self.verbose = kwargs.get('verbose', False)
        self.dir_current = os.getcwd()
        self.index_filename = 'index.html'
        self.feed_limit = 10
        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        cwd = self.dir_current
        self.dir_content = path.join(cwd, 'content', required=True)
        self.config = Config(path.join(cwd, 'site.yaml', required=True))

        self.dir_templates = path.join(cwd, 'templates', required=True)
        self.template = Template(self)

        self.dir_bin = path.join(cwd, 'bin')

        # make all settings in site section available to templates
        self.template.vars.update(self.config.section('site'))

        # Optional directory with static files like css, js and images.
        self.dir_static = path.join(cwd, 'static')

        # Directory is created by the generate command.
        self.dir_dst = path.join(cwd, 'deploy')

        self.base_url = self.config.get('site', 'base_url')
        # base_url must be defined in settings
        if not self.base_url:
            raise Exception('base_url not set in site config.')

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)

    def get_doc_template(self, doc):
        """Get template setting from doc otherwise from configuration."""

        template = self.config.search_dict_list(
            'templates', 'doc', 'content_type', 'template')

        return doc.get('template', template)

    def _update_indexes(self, doc, url=None):
        """Add a doc to indexes determined from given url.

        For each directory in the URL except for the one containing the content
        file itself an index is created, if it doesn't exist, and the document
        is added to the list of docs in the index.
        """

        if url is None:
            url = doc['url']

        dirs = path.list_dirs_from_url(url)
        for i, _ in enumerate(dirs):
            fullpath = '/'.join(dirs[:i+1])
            self.indexes[fullpath] = self.indexes.get(fullpath, []) + [doc]

    def update_indexes(self, doc):
        """Add all indexes for doc determined from headers."""

        # don't index documents with noindex set
        if 'noindex' in doc and doc['noindex']:
            return
        self._update_indexes(doc)
        # add to special __index__ for RSS generation
        self._update_indexes(doc, '__index__/index/')

        doc_indexes = self.config.section('indexes')
        for idx in doc_indexes:
            if idx['var'] in doc:
                self.update_doc_index(doc, idx['var'], idx['path'])

    def update_doc_index(self, doc, var, basepath):
        """Add the doc to the index defined for the header variable (var)."""

        for val in doc[var]:
            url = '/{}/{}/'.format(basepath, path.slugify(val))

            links = var + '_links'
            doc[links] = doc.get(links, []) + [(url, val)]

            # Must append file name to url to create subdir.
            self._update_indexes(doc, url + self.index_filename)

    def build_indexes(self, mode=None):
        """Build indexes of documents for content directories to be created.

        The mode argument hints the Logya command that was executed."""

        # a dictionary of indexes with parsed documents
        self.indexes = {}
        msg_duplicate = 'The URL {} is already used and will be overwritten.'

        for doc in DocReader(self.dir_content).parsed:
            url = doc['url']
            # warn user about duplicate URLs when not in serve mode
            if 'serve' != mode and url in self.docs_parsed:
                print(msg_duplicate.format(url))
            self.docs_parsed[url] = doc
            self.update_indexes(doc)

        # sort indexes by descending docs creation dates
        for idx in self.indexes:
            self.indexes[idx] = sorted(self.indexes[idx],
                                       key=itemgetter('created'),
                                       reverse=True)

        # make indexes available to templates
        self.template.vars['indexes'] = self.indexes

    def index_title(self, s):
        """Title for index pages, usually created from directory paths."""

        return ' » '.join(s.split('/')).replace('-', ' ').title()

    def write_rss(self, feed_title, directory, docs):
        """Write RSS 2.0 XML file in target directory"""

        self.template.vars['url'] = self.base_url
        self.template.vars['title'] = feed_title
        self.template.vars['description'] = directory
        self.template.vars['last_build'] = datetime.datetime.now()
        self.template.vars['items'] = docs[0:self.feed_limit]

        writer = FileWriter()
        page = self.template.env.get_template('rss2.xml')
        fh = writer.file_handle(self.dir_dst, path.join(directory, 'rss.xml'))
        writer.write(fh, page.render(self.template.vars))

    def write_index(self, filewriter, directory, template):
        """Write an auto-generated index.html file."""

        url = '/{}'.format(path.join(directory, self.index_filename))
        # make sure there exists no document at the index url
        if url not in self.docs_parsed:
            # Remove file name part if it's index.html, url ends with slash.
            url = url.replace(self.index_filename, '')

            docs = self.indexes[directory]

            # Ugly fix for issue #32: delete description var. This is called
            # for every index, instead of once for all, because write_index is
            # called in serve mode. Also there may remain other vars causing
            # future problems.
            # Emptying the vars dict does not work either, because the indexes
            # key is set in build_indexes and needed.
            if 'description' in self.template.vars:
                del self.template.vars['description']

            title = self.index_title(directory)

            self.template.vars['url'] = url
            self.template.vars['canonical'] = self.base_url + url
            self.template.vars['index'] = docs
            self.template.vars['title'] = title
            self.template.vars['directory'] = directory

            page = self.template.env.get_template(template)
            filewriter.write(filewriter.file_handle(self.dir_dst, directory),
                             page.render(self.template.vars))

            # write directory RSS file
            self.write_rss(title, directory, docs)

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists.

        If no template file is specified in configuration indexes won't be
        written.
        """

        template = self.config.search_dict_list(
            'templates', 'index', 'content_type', 'template')
        if not template:
            return

        feed_title = self.config.get('site', 'feed_title')
        if not feed_title:
            feed_title = 'RSS Feed'

        for directory in list(self.indexes.keys()):
            self.write_index(FileWriter(), directory, template)

        # write root RSS file
        if '__index__' in self.indexes:
            docs = sorted(self.indexes['__index__'],
                          key=itemgetter('created'),
                          reverse=True)
            self.write_rss(feed_title, '', docs)

    # TODO remove in 4.0
    def get_execs(self, dirname):
        """Generator yielding paths to executable files in given directory."""

        for p in os.listdir(dirname):
            fpath = path.join(dirname, p)
            if os.path.isfile(fpath) and os.access(fpath, os.X_OK):
                yield fpath

    # TODO remove in 4.0
    def exec_bin(self):
        """Execute binary files in bin dir."""

        dir_bin = path.join('bin')
        if os.path.exists(dir_bin):
            args = {'logya': self}
            for exe in self.get_execs(dir_bin):
                execfile(exe, args)
