# -*- coding: utf-8 -*-
import os
import datetime
import PyRSS2Gen
from operator import itemgetter
from config import Config
from docreader import DocReader
from docparser import DocParser
from template import Template
from writer import FileWriter

__version__ = '2.0dev'


class Logya(object):
    """Main logic for creating, building and serving a static site."""

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        if 'verbose' in kwargs and kwargs['verbose']:
            self.verbose = True
        else:
            self.verbose = False

        self.dir_current = os.getcwd()

        self.index_filename = 'index.html'

        self.feed_limit = 10

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        self.dir_content = self.get_path('content', required=True)
        self.config = Config(self.get_path('site.cfg', required=True))

        dir_templates = self.get_path('templates', required=True)
        self.template = Template(dir_templates)

        # make all settings in site section available to templates
        for key, val in self.config.items('site'):
            self.template.add_var(key, val)

        # optional directory with static files like style sheets, scripts and images
        self.dir_static = self.get_path('static')

        self.dir_dst = self.get_path('deploy')

        # feeds are only generated, if base_url is set in site section of config
        self.base_url = self.config.get('site', 'base_url')

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print msg

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

        if 'template' in doc:
            template = doc['template']
        else:
            template = self.config.get('templates', 'doc')
        return template

    def get_dirs_from_path(self, url):
        """Returns a list of directories from given url.

        The last directory is omitted as it contains and index.html file
        containing the content of the appropriate document."""

        return filter(None, url.strip('/').split('/'))[:-1]

    def update_index(self, doc, index):
        """Add a doc to given index."""

        if index not in self.indexes:
            self.indexes[index] = []
        self.indexes[index].append(doc)

    def update_indexes(self, doc):
        """Add a doc to indexes determined from doc url."""

        dirs = self.get_dirs_from_path(doc['url'])
        last = 0
        for d in dirs:
            last += 1
            self.update_index(doc, '/'.join(dirs[:last]))

    def build_indexes(self):
        """Build indexes of documents for content directories to be created."""

        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

        # a dictionary of indexes with parsed documents
        self.indexes = {}

        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            # ignore documents that have no url
            if 'url' not in doc:
                continue
            self.update_indexes(doc)
            self.docs_parsed[doc['url']] = doc

        # make indexes available to templates
        self.template.add_var('indexes', self.indexes)

    def write_rss(self, directory, docs):
        """Write RSS 2.0 XML file in target directory"""

        items = []
        for d in docs[0:self.feed_limit]:
            # omit start page
            if '/' == d['url']:
                continue

            url = self.base_url + d['url']
            title = d['title']

            description = title
            # TODO make sure description is set in Parser class
            if 'description' in d:
                description = d['description']

            items.append(PyRSS2Gen.RSSItem(
                title = title,
                link = url,
                description = description,
                guid = url,
                pubDate = d['created']))

        rss = PyRSS2Gen.RSS2(
            title = directory,
            link = self.base_url + os.path.join('/', directory, 'rss.xml'),
            description = directory,
            lastBuildDate = datetime.datetime.now(),
            items = items)

        rss_file_name = os.path.join(self.dir_dst, directory, 'rss.xml')
        rss_file = open(rss_file_name, 'w')
        rss.write_xml(rss_file)
        rss_file.close()

    def write_index(self, filewriter, directory, template):
        """Write an auto-generated index.html file."""

        url_path = '/%s' % os.path.join(directory, self.index_filename)
        # make sure there exists no document at the index path
        if url_path not in self.docs_parsed:
            docs = sorted(self.indexes[directory],
                          key=itemgetter('created'),
                          reverse=True)

            self.template.add_var('index', docs)
            self.template.add_var('directory', directory)

            page = self.template.get_env().get_template(template)
            filewriter.write(filewriter.getfile(self.dir_dst, directory),
                             page.render(self.template.get_vars())
                             .encode('utf-8'))

            # write directory RSS file
            if self.base_url:
                self.write_rss(directory, docs)

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists.

        If there is no template file specified in configuration indexes won't be written.
        """

        template = self.config.get('templates', 'index')
        if not template:
            return

        for directory in self.indexes.keys():
            self.write_index(FileWriter(), directory, template)

        # write root RSS file
        if self.base_url:
            docs = sorted(self.docs_parsed.values(),
                          key=itemgetter('created'),
                          reverse=True)
            self.write_rss('', docs)
