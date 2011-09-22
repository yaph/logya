# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil
import ConfigParser

dir_src = sys.path[0]
sys.path.append(os.path.join(dir_src, 'lib'))
from docwriter import DocWriter
from jinja2 import Environment, BaseLoader, TemplateNotFound

class Geeklog():

    def __init__(self):
        self.dir_src = dir_src
        self.dir_current = os.getcwd()
        self.dir_dst = os.path.join(self.dir_current, 'deploy')

    def create(self, site_name):
        src = os.path.join(self.dir_src, 'sites', 'geeksta') # TODO make docs default site
        dst = os.path.join(self.dir_current, site_name)
        shutil.copytree(src, dst)

    def generate():
        src_site = 'geeksta' # TODO use command, e.g. ./geeklog run .
        src = os.path.join(self.dir_src, 'sites', src_site)

        config = ConfigParser.ConfigParser()
        config.readfp(open(os.path.join(src, 'site.cfg')))
        base_path = config.get('site', 'base_path')

        dir_templates = os.path.join(src, 'templates')
        template_env = Environment(loader=GeeklogLoader(dir_templates))

        doc = DocWriter(base_path, template_env)
        docs = glob.glob(os.path.join(src, 'content', '*.html'))
        doc.writedocs(docs)

#        # copy static files
#        src_static = os.path.join(src, 'static')
#        dst_static = os.path.join(cwd, 'site', 'static')
#        shutil.rmtree(dst_static, True)
#        shutil.copytree(src_static, dst_static)

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
