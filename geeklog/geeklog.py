# -*- coding: utf-8 -*-
import os
import sys
import shutil
import config
from docreader import DocReader
from docparser import DocParser
from docwriter import DocWriter
from server import GeeklogServer
from jinja2 import Environment, BaseLoader, TemplateNotFound

class Geeklog():

    def __init__(self):
        self.dir_src = sys.path[0]
        self.dir_current = os.getcwd()

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
        self.template_env = Environment(loader=GeeklogLoader(dir_templates))

        self.dir_dst = os.path.join(self.dir_current, 'deploy')
        if not os.path.exists(self.dir_dst):
            os.makedirs(self.dir_dst)

    def copy_static(self):
        """Copy static files from source to deploy."""

        src_static = os.path.join(self.dir_current, 'static')
        dst_static = os.path.join(self.dir_dst, 'static')
        shutil.rmtree(dst_static, True)
        shutil.copytree(src_static, dst_static)

    def create(self, site_name):
        """Create a basic template for generating a Web site with geeklog."""

        src = os.path.join(self.dir_src, 'sites', 'geeksta') # TODO make docs default site
        dst = os.path.join(self.dir_current, site_name)
        shutil.copytree(src, dst)

    # TODO implement incremental site generation
    def generate(self):
        """Generate a Web site to deploy from the current directory as the source."""

        self.init_env()
        print "Generating site in directory: %s" % self.dir_dst

        base_path = self.config.get('site', 'base_path')
        dw = DocWriter(self.dir_dst, self.template_env, base_path)
        docs = DocReader(self.dir_content).get_docs()
        for doc in docs:
            dw.write(DocParser(doc))

        self.copy_static()

    def serve(self):
        GeeklogServer(self, 'localhost', 8080).serve()

    def test(self):
        self.init_env()
        docs = DocReader(self.dir_content).get_docs()
        for doc in docs:
            dp = DocParser(doc)
            print dp

class GeeklogLoader(BaseLoader):

    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = os.path.join(self.path, template)
        if not os.path.exists(path):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        with file(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambda: mtime == os.path.getmtime(path)
