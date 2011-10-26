# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, BaseLoader, TemplateNotFound

class Template():

    def __init__(self, dir_templates):
        self.vars = {}
        self.dir_templates = dir_templates
        self.env = Environment(loader=TemplateLoader(self.dir_templates))

    def get_env(self):
        return self.env

    def add_var(self, name, value):
        self.vars[name] = value

    def get_var(self, name):
        return self.vars[name]

    def get_vars(self):
        return self.vars

class TemplateLoader(BaseLoader):

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
