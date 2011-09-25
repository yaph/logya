# -*- coding: utf-8 -*-
from jinja2 import Environment, BaseLoader, TemplateNotFound

class Template():

    def __init__(self):
        self.vars = {}

    def add_var(self, name, value):
        self.vars[name] = value

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
