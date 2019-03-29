#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program flattens the content hierarchy of documents generated using the write_content function.
# It creates markdown versions from files named index.html in the directory content_new. New files get
# the name of their parent directory.
import os

from html2text import html2text

from logya.core import Logya
from logya.writer import encode_content, write


L = Logya()
L.init_env()
L.build_index()

for url, doc in L.docs.items():
    content_file = os.path.join(L.dir_content, url.strip('/'), 'index.html')
    if os.path.exists(content_file):
        body = html2text(doc['body'])

        # Cleanup
        del doc['body']
        if 'tags_links' in doc:
            del doc['tags_links']

        content = encode_content(doc, body)
        target_file = os.path.dirname(content_file) + '.md'

        write(target_file.replace('/content/', '/content_new/'), content)