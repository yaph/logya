# -*- coding: utf-8 -*-
import os
import shutil

from logya.core import Logya
from logya.fs import copytree
from logya.writer import DocWriter


class Generate(Logya):
    """Generate a Web site to public from current directory as source."""

    def __init__(self, **kwargs):
        super(Generate, self).__init__(**kwargs)
        self.init_env()
        self.writer = DocWriter(self.dir_public, self.template)

        if not kwargs.get('keep'):
            self.info('Remove existing public directory')
            shutil.rmtree(self.dir_public, True)

        self.info('Generate site in directory: {}'.format(self.dir_public))
        if os.path.exists(self.dir_static):
            self.info('Copy static files')
            copytree(self.dir_static, self.dir_public)

        self.build()
        self.write()

    def build(self):
        self.info('Build document index')
        self.build_index()

    def write(self):
        self.info('Write documents')
        for doc in self.docs.values():
            self.writer.write(doc, self.get_doc_template(doc))
        self.info(
            'Written {:d} documents to public directory'
            .format(len(self.docs)))

        self.info('Write index files')
        self.write_index_files()
        self.info(
            'Written {:d} index files to public directory'
            .format(len(self.index)))
