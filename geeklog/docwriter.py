# -*- coding: utf-8 -*-
import os

class DocWriter:

    def __init__(self, dir_dst, template):
        self.dir_dst = dir_dst
        self.template = template

    def set_template_vars(self, doc):
        self.template.add_var('body', doc.getbody().decode('utf-8'))
        self.template.add_var('title', doc.getheader('title').decode('utf-8'))
        self.template.add_var('scripts', doc.getscripts())
        self.template.add_var('styles', doc.getstyles())
        self.template.add_var('template', doc.getheader('template'))

    def getfile(self, doc):
        url = doc.getheader('url')
        # TODO if url ends with a file exension like .html generate a file of that name
        directory = os.path.join(self.dir_dst, url.lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)
        return open(os.path.join(directory, 'index.html'), 'w')

    def write(self, doc):
        self.set_template_vars(doc)
        page = self.template.get_env().get_template(doc.getheader('template'))
        f = self.getfile(doc)
        f.write(page.render(self.template.get_vars()).encode('utf-8'))
