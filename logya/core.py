# -*- coding: utf-8 -*-
import os
import re
import datetime
from operator import itemgetter

from logya.compat import execfile
from logya.config import Config
from logya.docreader import DocReader
from logya.docparser import DocParser
from logya.template import Template
from logya.writer import FileWriter


class Logya(object):
    """Main logic for creating, building and serving a static site."""

    re_url_replace = re.compile(r'[\s_]+')

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        if 'verbose' in kwargs and kwargs['verbose']:
            self.verbose = True
        else:
            self.verbose = False

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

        self.dir_content = self.get_path('content', required=True)
        self.config = Config(self.get_path('site.yaml', required=True))

        dir_templates = self.get_path('templates', required=True)
        self.template = Template(dir_templates)

        self.dir_bin = self.get_path('bin')

        # make all settings in site section available to templates
        for key, val in list(self.config.get_section('site').items()):
            self.template.add_var(key, val)

        # optional directory with static files like css, js and images
        self.dir_static = self.get_path('static')

        self.dir_dst = self.get_path('deploy')

        # feeds are only generated, if base_url is set in site section of config
        self.base_url = self.config.get('site', 'base_url')

        if self.base_url is False:
            raise Exception('base_url not set in site config.')

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)

    def set_dir_current(self, dir_current):
        """Called from tests."""

        self.dir_current = dir_current

    def get_path(self, name, required=False):
        """Get path relative to current working directory for given name.

        Raises an exception if resource is required and doesn't exist.
        """

        path = os.path.join(self.dir_current, name)
        if required and not os.path.exists(path):
            raise Exception('Resource at path "%s" does not exist.' % path)
        return path

    def get_doc_template(self, doc):
        """Try to get template setting from doc otherwise from configuration."""

        template = self.config.get_item(
            'templates', 'doc', 'content_type', 'template')

        return doc.get('template', template)

    def get_dirs_from_path(self, url):
        """Returns a list of directories from given url.

        The last directory is omitted as it contains and index.html file
        containing the content of the appropriate document."""

        dirs = [f for f in url.strip('/').split('/') if f]
        if dirs:
            dirs = dirs[:-1]
        return dirs

    def update_index(self, doc, path):
        """Add a doc to given path index."""

        self.indexes[path] = self.indexes.get(path, []) + [doc]

    def _update_indexes(self, doc, url=None):
        """Add a doc to indexes determined from given url."""

        if url is None:
            url = doc['url']

        dirs = self.get_dirs_from_path(url)
        last = 0
        for d in dirs:
            last += 1
            self.update_index(doc, '/'.join(dirs[:last]))

    def update_indexes(self, doc):
        """Add all indexes for doc determined from headers."""

        # don't index documents with noindex set
        if 'noindex' in doc and doc['noindex']:
            return
        self._update_indexes(doc)
        # add to special __index__ for RSS generation
        self._update_indexes(doc, '__index__/index/')

        doc_indexes = self.config.get_section('indexes')
        for idx in doc_indexes:
            if idx['var'] in doc:
                self.update_doc_index(doc, idx['var'], idx['path'])

    def update_doc_index(self, doc, var, path):
        """Update doc index."""

        for val in doc[var]:
            var_path = re.sub(self.re_url_replace, '-', val).lower()
            url = '/%s/%s/' % (path, var_path)
            links = var + '_links'
            doc[links] = doc.get(links, []) + [(url, val)]
            # must append path after tag string to create subdir
            self._update_indexes(doc, url + self.index_filename)

    def build_indexes(self, mode=None):
        """Build indexes of documents for content directories to be created."""

        # a dictionary of indexes with parsed documents
        self.indexes = {}

        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            # ignore empty documents and those without url
            if doc is None or 'url' not in doc:
                continue
            url = doc['url']
            # warn user about duplicate URLs when not in serve mode
            if 'serve' != mode and url in self.docs_parsed:
                print(('The URL %s is already used and will be overwritten.'
                    % url))
            self.docs_parsed[url] = doc

        for doc in list(self.docs_parsed.values()):
            self.update_indexes(doc)

        # sort indexes by descending docs creation dates
        for idx in self.indexes:
            self.indexes[idx] = sorted(self.indexes[idx],
                                       key=itemgetter('created'),
                                       reverse=True)

        # make indexes available to templates
        self.template.add_var('indexes', self.indexes)

    def index_title(self, s):
        """Title for index pages, usually created from directory paths."""

        return ' » '.join(
            s.split('/')).replace('-', ' ').title().decode('utf-8')

    def write_rss(self, feed_title, directory, docs):
        """Write RSS 2.0 XML file in target directory"""

        self.template.add_var('url', self.base_url)
        self.template.add_var('title', feed_title)
        self.template.add_var('description', directory)
        self.template.add_var('last_build', datetime.datetime.now())
        self.template.add_var('items', docs[0:self.feed_limit])

        writer = FileWriter()
        page = self.template.env.get_template('rss2.xml')
        fh = writer.getfile(self.dir_dst, os.path.join(directory, 'rss.xml'))
        writer.write(fh, page.render(self.template.get_vars()))

    def write_index(self, filewriter, directory, template):
        """Write an auto-generated index.html file."""

        url_path = '/%s' % os.path.join(directory, self.index_filename)
        # make sure there exists no document at the index path
        if url_path not in self.docs_parsed:
            docs = self.indexes[directory]

            # remove the file name part if it's index.html
            url = url_path.replace(self.index_filename, '')
            self.template.add_var('url', url)
            self.template.add_var('canonical', self.base_url + url)
            self.template.add_var('index', docs)
            self.template.add_var('title', self.index_title(directory))
            self.template.add_var('directory', directory)

            page = self.template.env.get_template(template)
            filewriter.write(filewriter.getfile(self.dir_dst, directory),
                             page.render(self.template.get_vars()))

            # write directory RSS file
            if self.base_url:
                self.write_rss(self.index_title(directory), directory, docs)

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists.

        If no template file is specified in configuration indexes won't be
        written.
        """

        template = self.config.get_item(
            'templates', 'index', 'content_type', 'template')
        if not template:
            return

        feed_title = self.config.get('site', 'feed_title')
        if not feed_title:
            feed_title = 'RSS Feed'

        for directory in list(self.indexes.keys()):
            self.write_index(FileWriter(), directory, template)

        # write root RSS file
        if self.base_url:
            docs = sorted(self.indexes['__index__'],
                          key=itemgetter('created'),
                          reverse=True)
            self.write_rss(feed_title, '', docs)

    def get_execs(self, path):
        """Generator yielding paths to executable files in given directory."""

        for p in os.listdir(path):
            fpath = os.path.join(path, p)
            if os.path.isfile(fpath) and os.access(fpath, os.X_OK):
                yield fpath

    def exec_bin(self):
        """Execute binary files in bin dir."""

        dir_bin = self.get_path('bin')
        if os.path.exists(dir_bin):
            args = {'logya': self}
            for exe in self.get_execs(dir_bin):
                execfile(exe, args)