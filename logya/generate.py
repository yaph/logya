# -*- coding: utf-8 -*-
import os
import shutil
from operator import itemgetter
from logya import Logya
from docreader import DocReader
from docparser import DocParser
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
            dw.write(doc)

        self.info("Write indexes")
        self.write_indexes()

    def get_dirs_from_path(self, url):
        """Returns a list of directories from given url.

        The last directory is omitted as it contains and index.html file
        containing the content of the appropriate document."""

        return filter(None, url.strip('/').split('/'))[:-1]

    def update_index(self, doc, index):
        """Add a doc to given index."""

        if not self.indexes.has_key(index):
            self.indexes[index] = []
        self.indexes[index].append(doc)

    def update_indexes(self, doc):
        """Add a doc to indexes determined from doc url."""

        dirs = self.get_dirs_from_path(doc['url'])
        last = 0
        for d in dirs:
            last += 1
            self.update_index(doc, '/'.join(dirs[:last]))

    def build_indexes(self):
        """Build indexes of documents for content directories to be created."""

        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            # ignore documents that have no url
            if not doc.has_key('url'):
                continue
            self.update_indexes(doc)
            self.docs_parsed[doc['url']] = doc

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
                fw.write(file, page.render(index=docs, title=dir).encode('utf-8'))
