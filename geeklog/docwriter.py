# -*- coding: utf-8 -*-
import os

class DocWriter:

    def __init__(self, dir_dst, template_env, base_path):
        self.dir_dst = dir_dst
        self.template_env = template_env
        self.base_path = base_path

    def getfile(self, doc):
        url = doc.getheader('url')
        directory = os.path.join(self.dir_dst, url.lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)
        return open(os.path.join(directory, 'index.html'), 'w')

    def write(self, doc):
        body = doc.getbody().decode('utf-8')
        title = doc.getheader('title').decode('utf-8')
        scripts = doc.getscripts()
        styles = doc.getstyles()
        template = doc.getheader('template')
        page = self.template_env.get_template(template)
        f = self.getfile(doc)
        c = page.render(
            title=title,
            body=body,
            base_path=self.base_path,
            styles=styles,
            scripts=scripts)
        f.write(c.encode('utf-8'))
