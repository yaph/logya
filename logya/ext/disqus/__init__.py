# -*- coding: utf-8 -*-
# see https://github.com/jarodl/disqus.py
from ext import Extension

def main():
    return Disqus()

class Disqus(Extension):

    def get_type(self):
        return 'doc'

    def process(self, doc):
        print self.get_directory()
