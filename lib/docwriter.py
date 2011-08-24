import os
from docparser import DocParser

class DocWriter:
    def __init__(self, filename):
        self.doc = DocParser(filename)
        self.cwd = os.getcwd()

    def getfile(self):
        url = self.doc.getheader('url')
        directory = os.path.join(self.cwd, 'site', url.lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)
        return open(os.path.join(directory, 'index.html'), 'w')

    def write(self):
        body = self.doc.getbody()
        scripts = self.doc.getscripts()
        f = self.getfile()
        f.write(body)
