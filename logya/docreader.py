# -*- coding: utf-8 -*-
import os
import glob

class DocReader():

    def __init__(self, dir_base, parser):
        self.dir_base = dir_base
        self.parser = parser
        # TODO recurse through sub directories
        self.files = []
        for root, dirs, files in os.walk(self.dir_base):
            self.files.extend([os.path.join(root, f) for f in files])


    def get_docs(self):
        """Generator that reads all docs from base directory."""

        for f in self.files:
            yield self.parser.parse(f)