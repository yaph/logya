# -*- coding: utf-8 -*-
import os
import shutil

from logya.core import Logya
from logya.writer import DocWriter


class Generate(Logya):
    """Generate a Web site to deploy from current directory as source."""

    def __init__(self, **kwargs):

        super(self.__class__, self).__init__(**kwargs)
        self.init_env()

        # init writer before executing scripts, so they can use it
        self.writer = DocWriter(self.dir_dst, self.template)

        self.info("Remove existing deploy directory")
        shutil.rmtree(self.dir_dst, True)

        self.info("Generating site in directory: %s" % self.dir_dst)

        if os.path.exists(self.dir_static):
            self.info("Copy static files")
            shutil.copytree(self.dir_static, self.dir_dst)

        # execute scripts in before building indexes, so that generated content
        # can be indexed too
        self.info("Execute scripts in bin dir")
        self.exec_bin()

        self.info("Build document indexes")
        self.build_indexes()

        #template_env = self.template.get_env()
        #template_env.globals['__docs__'] = self.docs_parsed

        self.info("Write documents to deploy directory")
        for doc in list(self.docs_parsed.values()):
            self.writer.write(doc, self.get_doc_template(doc))

        self.info("Write indexes")
        self.write_indexes()