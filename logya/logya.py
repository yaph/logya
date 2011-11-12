# -*- coding: utf-8 -*-
import os
from operator import itemgetter
from config import Config
from docreader import DocReader
from docparser import DocParser
from template import Template
from writer import FileWriter

class Logya(object):
    """Main logic for creating, building and serving a static site."""

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        if kwargs.has_key('verbose') and kwargs['verbose']:
            self.verbose = True
        else:
            self.verbose = False

        self.dir_current = os.getcwd()

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        self.dir_content = self.get_path('content', required=True)
        self.config = Config(self.get_path('site.cfg', required=True))

        dir_templates = self.get_path('templates', required=True)
        self.template = Template(dir_templates)
        self.template.add_var('base_path', self.config.get('site', 'base_path'))

        # optional directory with static files like style sheets, scripts and images
        self.dir_static = self.get_path('static')

        self.dir_dst = self.get_path('deploy')

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

        if doc.has_key('template'):
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

        if not self.indexes.has_key(index):
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
            if not doc.has_key('url'):
                continue
            self.update_indexes(doc)
            self.docs_parsed[doc['url']] = doc

        # make indexes available to templates
        self.template.add_var('indexes', self.indexes)

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists.

        If there is no template file specified in configuration indexes won't be written.
        """

        template = self.config.get('templates', 'index')
        if not template:
            return

        filename = 'index.html'

        for dir, docs in self.indexes.items():
            url_path = '/%s' % os.path.join(dir, filename)
            # make sure there exists no document at the index path
            if not self.docs_parsed.has_key(url_path):
                docs = sorted(docs, key=itemgetter('created'), reverse=True)
                page = self.template.get_env().get_template(template)

                self.template.add_var('index', docs)
                self.template.add_var('title', dir)

                fw = FileWriter()
                file = fw.getfile(os.path.join(self.dir_dst, dir), filename)
                fw.write(file, page.render(self.template.get_vars()).encode('utf-8'))