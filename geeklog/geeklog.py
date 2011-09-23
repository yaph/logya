# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil
import config
from docwriter import DocWriter
from server import GeeklogServer, GeeklogHTTPRequestHandler
from jinja2 import Environment, BaseLoader, TemplateNotFound

class Geeklog():

    def __init__(self):
        self.dir_src = sys.path[0]
        self.dir_current = os.getcwd()


    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and later used object properties, and checks if required
        files and directories exist.
        """

        file_conf = os.path.join(self.dir_current, 'site.cfg')
        if not os.path.exists(file_conf):
            raise Exception('Configuration file does not exist.')
        self.config = config.get(file_conf)

        self.dir_content = os.path.join(self.dir_current, 'content')
        if not os.path.exists(self.dir_content):
            raise Exception('Content directory does not exist.')

        self.dir_static = os.path.join(self.dir_current, 'static')
        if not os.path.exists(self.dir_static):
            raise Exception('Static files directory does not exist.')

        dir_templates = os.path.join(self.dir_current, 'templates')
        if not os.path.exists(dir_templates):
            raise Exception('Template directory does not exist.')
        self.template_env = Environment(loader=GeeklogLoader(dir_templates))

        self.dir_dst = os.path.join(self.dir_current, 'deploy')
        if not os.path.exists(self.dir_dst):
            os.makedirs(self.dir_dst)


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

        doc = DocWriter(self.dir_dst, self.template_env, base_path)
        # TODO recurse through sub directories
        docs = glob.glob(os.path.join(self.dir_content, '*.html'))
        doc.writedocs(docs)

        # copy static files
        src_static = os.path.join(self.dir_current, 'static')
        dst_static = os.path.join(self.dir_dst, 'static')
        shutil.rmtree(dst_static, True)
        shutil.copytree(src_static, dst_static)


    def serve(self):
        GeeklogServer(self, 'localhost', 8080).serve()


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
