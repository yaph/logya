# -*- coding: utf-8 -*-
import os
import glob

class DocReader():

    def __init__(self, dir_base, parser):
        self.dir_base = dir_base
        self.parser = parser
        # TODO recurse through sub directories
        self.files = glob.glob(os.path.join(self.dir_base, '*.html'))

    def get_docs(self):
        """Generator that reads all docs from base directory."""

        for f in self.files:
            yield self.parser.parse(f)