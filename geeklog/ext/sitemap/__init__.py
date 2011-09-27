# -*- coding: utf-8 -*-
from ext import Extension

def main():
    return Sitemap()

class Sitemap(Extension):

    def get_type(self):
        return 'index'

    def process(self, index):
        print index
