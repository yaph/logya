# -*- coding: utf-8 -*-
import os
from docparser import DocParser

class DocWriter:
    def __init__(self, filename, template_env):
        self.doc = DocParser(filename)
        self.cwd = os.getcwd()
        self.template_env = template_env

    def getfile(self):
        url = self.doc.getheader('url')
        directory = os.path.join(self.cwd, 'site', url.lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)
        return open(os.path.join(directory, 'index.html'), 'w')

    def write(self):
        body = self.doc.getbody().decode('utf-8')
        title = self.doc.getheader('title').decode('utf-8')
        scripts = self.doc.getscripts()
        template = self.doc.getheader('template')
        page = self.template_env.get_template(template)
        f = self.getfile()
        c = page.render(title=title, body=body)
        f.write(c.encode('utf-8'))
