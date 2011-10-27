# -*- coding: utf-8 -*-
import os
import sys
import shutil
import config
from operator import itemgetter
from common import deprecated
from docreader import DocReader
from docparser import DocParser
from docwriter import DocWriter
from template import Template
from server import Server

class Logya:
    """Class with main logic for creating, building and serving a static Web site."""

    def __init__(self):
        # a list of parsed documents indexed by resource paths
        self.docs_parsed = []

        # a dictionary of indexes with parsed documents
        self.indexes = {}

        self.dir_src = sys.path[0]
        self.dir_current = os.getcwd()

    def set_dir_current(self, dir_current):
        """Called from tests."""

        self.dir_current = dir_current

    def test_and_get_path(self, name):
        """Test whether resource exists at path relative to current directory and return its full path."""

        path = os.path.join(self.dir_current, name)
        if not os.path.exists(path):
            raise Exception('Path "%s" does not exist.' % path)
        return path

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        file_conf = self.test_and_get_path('site.cfg')
        self.config = config.get(file_conf)

        self.dir_content = self.test_and_get_path('content')
        self.dir_static = self.test_and_get_path('static')

        dir_templates = self.test_and_get_path('templates')
        self.template = Template(dir_templates)
        self.template.add_var('base_path', self.config.get('site', 'base_path'))

        self.dir_dst = os.path.join(self.dir_current, 'deploy')

    def create(self, site_name):
        """Create a basic template for generating a Web site with Logya."""

        src = os.path.join(self.dir_src, 'sites', 'geeksta') # TODO make docs default site
        dst = os.path.join(self.dir_current, site_name)
        shutil.copytree(src, dst)

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

        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            # ignore documents that have no url
            if not doc.has_key('url'):
                continue
            self.update_indexes(doc)
            self.docs_parsed.append(doc)

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists."""

        template = self.config.get('templates', 'index')

        for dir, docs in self.indexes.items():
            index_file = os.path.join(self.dir_dst, dir, 'index.html')
            # FIXME check whether a document from content dir exists at target
            # so generated indexes can be overwritten
            if not os.path.exists(index_file):
                docs = sorted(docs, key=itemgetter('created'), reverse=True)
                page = self.template.get_env().get_template(template)
                file = open(index_file, 'w')
                file.write(page.render(index=docs, title=dir).encode('utf-8'))
                file.close()

    def generate(self):
        """Generate a Web site to deploy from the current directory as the source."""

        self.init_env()
        print "Generating site in directory: %s" % self.dir_dst

        print "Remove existing deploy directory"
        shutil.rmtree(self.dir_dst, True)

        print "Copy static files"
        # has do take place before indexes are built
        shutil.copytree(os.path.join(self.dir_current, 'static'), self.dir_dst)

        print "Build document indexes"
        self.build_indexes()

        print "Write documents to deploy directory"
        dw = DocWriter(self.dir_dst, self.template)
        for doc in self.docs_parsed:
            dw.write(doc)

        print "Write indexes"
        self.write_indexes()

    def update_file(self, src, dst):
        """Copy source file to destination file if source is newer."""

        if os.path.getmtime(src) > os.path.getmtime(dst):
            shutil.copyfile(src, dst)
            return True
        return False

    def refresh_resource(self, path):
        """Refresh resource corresponding to given path.

        Static files are updated if necessary, documents are read, parsed and
        written to the corresponding destination in the deploy directory."""

        self.init_env()

        # if a file relative to static source is requested update it and return
        path_rel = path.lstrip('/')
        file_src = os.path.join(self.dir_current, path_rel)
        if os.path.isfile(file_src):
            file_dst = os.path.join(self.dir_dst, path_rel)
            if self.update_file(file_src, file_dst):
                return "Copied file %s to %s" % (file_src, file_dst)
            return "Source %s is not newer than destination %s" % (file_src, file_dst)

        # find doc that corresponds to path, regenerate it and return
        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            if not doc.has_key('url'):
                continue
            url = doc['url']
            # Is it the requested doc? Be forgiving about trailing slashes.
            if path.rstrip('/') == url.rstrip('/'):
                dw = DocWriter(self.dir_dst, self.template)
                dw.write(doc)
                return "Refreshed doc at URL: %s" % url

    def serve(self):
        """Serve files from deploy directory."""

        Server(self, 'localhost', 8080).serve()

    def test(self):
        """Test new features."""

        self.init_env()
        self.refresh_resource('/shop/')
#        from ext import ExtensionLoader
#        el = ExtensionLoader()
#        print el.get_by_type('doc')
#        print el.get_by_type('index')