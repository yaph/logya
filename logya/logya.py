# -*- coding: utf-8 -*-
import os
import sys
import shutil
import config
from common import deprecated
from docreader import DocReader
from docparser import DocParser
from docwriter import DocWriter
from template import Template
from server import Server

class Logya:
    """Class with main logic for creating, building and serving a static Web site."""

    def __init__(self):
        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

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
        if not os.path.exists(self.dir_dst):
            os.makedirs(self.dir_dst)

    @deprecated
    def get_docs_in_dir(self, dirpath):
        docs = []
        for url, doc in self.docs_parsed.items():
            if url.startswith(dirpath):
                docs.append(doc)
        return docs

    @deprecated
    def generate_index(self, dirpath):
        """Generate index.html files in deploy directories where non exists."""

        template = self.config.get('templates', 'index')
        index_file = os.path.join(dirpath, 'index.html')
        if not os.path.exists(index_file):
            resource_path = dirpath.replace(self.dir_dst, '')
            docs = self.get_docs_in_dir(resource_path)
            index = []
            for doc in docs:
                index.append({'title':doc['title'],
                              'url':doc['url']})
            page = self.template.get_env().get_template(template)
            file = open(index_file, 'w')
            file.write(page.render(index=index,title=resource_path.lstrip('/')).encode('utf-8'))

    @deprecated
    def generate_indexes(self):
        """Generate index.html files in all created directories.

        Files are only created if they do not exist yet.
        """

        # process all directories in deploy except static
        for path in os.listdir(self.dir_dst):
            start_path = os.path.join(self.dir_dst, path)
            if os.path.isdir(start_path) and 'static' != path:
                for dirpath, dirnames, filenames in os.walk(start_path):
                    self.generate_index(dirpath)

    def copy_static(self):
        """Copy static files from source to deploy."""

        src_static = os.path.join(self.dir_current, 'static')
        dst_static = os.path.join(self.dir_dst, 'static')
        shutil.rmtree(dst_static, True)
        shutil.copytree(src_static, dst_static)

    def create(self, site_name):
        """Create a basic template for generating a Web site with Logya."""

        src = os.path.join(self.dir_src, 'sites', 'geeksta') # TODO make docs default site
        dst = os.path.join(self.dir_current, site_name)
        shutil.copytree(src, dst)

    @deprecated
    def generate(self):
        """Generate a Web site to deploy from the current directory as the source."""

        self.init_env()
        print "Generating site in directory: %s" % self.dir_dst

        dw = DocWriter(self.dir_dst, self.template)
        docs = DocReader(self.dir_content).get_docs()
        dp = DocParser()
        for doc in docs:
            d = dp.parse(doc)
            url = d['url']
            self.docs_parsed[url] = d
            dw.write(d)

        self.generate_indexes()
        self.copy_static()

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

    def update_indexes(self, doc, path):
        """Add a doc to indexes determined given path."""

        dirs = self.get_dirs_from_path(path)
        last = 0
        for d in dirs:
            last += 1
            self.update_index(doc, '/'.join(dirs[:last]))

    def build_indexes(self):
        docs = DocReader(self.dir_content).get_docs()
        dp = DocParser()
        for doc in docs:
            d = dp.parse(doc)
            url = d['url']
            self.update_indexes(d, url)
            self.docs_parsed[url] = d

    def generate2(self):
        """Generate a Web site to deploy from the current directory as the source."""

        self.init_env()
        print "Generating site in directory: %s" % self.dir_dst

        self.build_indexes()
        for idx, docs in self.indexes.items():
            print idx
            for doc in docs:
                print doc['url']

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
        docs = DocReader(self.dir_content).get_docs()
        dp = DocParser()
        for doc in docs:
            d = dp.parse(doc)
            url = d['url']
            self.docs_parsed[url] = d
            # Is it the requested doc? Be forgiving about trailing slashes.
            if path.rstrip('/') == url.rstrip('/'):
                dw = DocWriter(self.dir_dst, self.template)
                dw.write(d)
                return "Refreshed doc at URL: %s" % url

    def serve(self):
        Server(self, 'localhost', 8080).serve()

    def test(self):
        self.init_env()
        self.refresh_resource('/shop/')
#        from ext import ExtensionLoader
#        el = ExtensionLoader()
#        print el.get_by_type('doc')
#        print el.get_by_type('index')