# -*- coding: utf-8 -*-
import os
import shutil
from __init__ import Logya
from writer import DocWriter


class Generate(Logya):
    """Generate a Web site to deploy from current directory as source."""

    def __init__(self, **kwargs):

        super(self.__class__, self).__init__(**kwargs)
        self.init_env()
        self.info("Generating site in directory: %s" % self.dir_dst)

        self.info("Remove existing deploy directory")
        shutil.rmtree(self.dir_dst, True)

        if os.path.exists(self.dir_static):
            self.info("Copy static files")
            shutil.copytree(self.dir_static, self.dir_dst)

        self.info("Build document indexes")
        self.build_indexes()

        self.info("Write documents to deploy directory")
        dw = DocWriter(self.dir_dst, self.template)
        for doc in self.docs_parsed.itervalues():
            dw.write(doc, self.get_doc_template(doc))

        self.info("Write indexes")
        self.write_indexes()
