# -*- coding: utf-8 -*-
import os
from docparser import DocParser

class DocWriter:
    def __init__(self, base_path, template_env):
        self.docs = []
        self.cwd = os.getcwd()
        self.base_path = base_path
        self.template_env = template_env

    def getfile(self, doc):
        url = doc.getheader('url')
        directory = os.path.join(self.cwd, 'site', url.lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)
        return open(os.path.join(directory, 'index.html'), 'w')

    def write(self, doc):
        body = doc.getbody().decode('utf-8')
        title = doc.getheader('title').decode('utf-8')
        scripts = doc.getscripts()
        template = doc.getheader('template')
        page = self.template_env.get_template(template)
        f = self.getfile(doc)
        c = page.render(title=title, body=body, base_path=self.base_path)
        f.write(c.encode('utf-8'))

    def writedocs(self, files):
        for f in files:
            doc = DocParser(f)
            self.docs.append(doc)
            self.write(doc)

