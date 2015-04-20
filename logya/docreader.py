# -*- coding: utf-8 -*-
import os
from logya.globals import allowed_exts
from logya.docparser import parse


class DocReader:
    '''A class for reading content documents.'''

    def __init__(self, dir_base):
        '''Recurse through content directory to add files to read and parse.'''

        self.dir_base = dir_base
        self.files = []
        for root, dirs, files in os.walk(self.dir_base):
            self.files.extend([
                os.path.join(root, f) for f in files
                if os.path.splitext(f)[1].strip('.') in allowed_exts
            ])

    @property
    def parsed(self):
        '''Generator that reads all docs from base directory.'''

        for f in self.files:
            yield parse(f)
