# -*- coding: utf-8 -*-
import os
import shutil
from operator import itemgetter
from logya import Logya
from writer import FileWriter, DocWriter

class Generate(Logya):
    """Generate a Web site to deploy from the current directory as the source."""

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

    def write_indexes(self):
        """Write index.html files to deploy directories where non exists.

        If there is no template file specified in configuration indexes won't be written.
        """

        template = self.config.get('templates', 'index')
        if not template:
            return

        filename = 'index.html'

        for dir, docs in self.indexes.items():
            url_path = '/%s' % os.path.join(dir, filename)
            # make sure there exists no document at the index path
            if not self.docs_parsed.has_key(url_path):
                docs = sorted(docs, key=itemgetter('created'), reverse=True)
                page = self.template.get_env().get_template(template)
                fw = FileWriter()
                file = fw.getfile(os.path.join(self.dir_dst, dir), filename)
                fw.write(file, page.render(index=docs, title=dir, indexes=self.indexes).encode('utf-8'))
