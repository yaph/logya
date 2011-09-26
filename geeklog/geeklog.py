# -*- coding: utf-8 -*-
import os
import sys
import shutil
import config
from docreader import DocReader
from docparser import DocParser
from docwriter import DocWriter
from template import Template
from server import GeeklogServer

class Geeklog():

    def __init__(self):
        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

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
        self.template = Template(dir_templates)
        self.template.add_var('base_path', self.config.get('site', 'base_path'))

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

        dw = DocWriter(self.dir_dst, self.template)
        docs = DocReader(self.dir_content).get_docs()
        for doc in docs:
            dp = DocParser(doc)
            url = dp.getheader('url')
            self.docs_parsed[url] = dp
            dw.write(dp)

        self.copy_static()

    def refresh_resource(self, path):
        """Refresh resource corresponding to given path.

        Static files are simply coypied, documents are read, parsed and 
        written to the corresponding destination in the deploy directory."""

        self.init_env()

        # if a file relative to static source is requested copy it and return
        path_rel = path.lstrip('/')
        file_src = os.path.join(self.dir_current, path_rel)
        if os.path.isfile(file_src):
            file_dst = os.path.join(self.dir_dst, path_rel)
            shutil.copyfile(file_src, file_dst)
            return "Copied file %s to %s" % (file_src, file_dst)

        # find doc that corresponds to path, regenerate it and return
        docs = DocReader(self.dir_content).get_docs()
        for doc in docs:
            dp = DocParser(doc)
            url = dp.getheader('url')
            self.docs_parsed[url] = dp
            # Is it the requested doc? Be forgiving about trailing slashes.
            if path.rstrip('/') == url.rstrip('/'):
                dw = DocWriter(self.dir_dst, self.template)
                dw.write(dp)
                return "Refreshed doc at URL: %s" % url

    def serve(self):
        GeeklogServer(self, 'localhost', 8080).serve()

    def test(self):
        self.refresh_resource('/static/js/script.js')

