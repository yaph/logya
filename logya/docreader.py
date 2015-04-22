# -*- coding: utf-8 -*-
import os

from datetime import datetime

from logya import allowed_exts
from logya.compat import file_open as open
from logya.docparser import parse


def content_type(filename):
    ctype = None
    ext = os.path.splitext(filename)[1]
    if ext in ['.html', '.htm']:
        ctype = 'html'
    elif ext in ['.md', '.markdown']:
        ctype = 'markdown'
    return ctype


class DocReader:
    """A class for reading content documents."""

    def __init__(self, dir_base):
        """Recurse through content directory to add files to read and parse."""

        self.dir_base = dir_base
        self.files = []
        for root, dirs, files in os.walk(self.dir_base):
            self.files.extend([
                os.path.join(root, f) for f in files
                if os.path.splitext(f)[1].strip('.') in allowed_exts
            ])

    def read(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()

    @property
    def parsed(self):
        """Generator that reads all docs from base directory and returns parsed
        content."""

        for filename in self.files:
            stat = os.stat(filename)
            content = self.read(filename)
            if content:
                yield parse(content,
                            modified=datetime.fromtimestamp(stat.st_mtime),
                            content_type=content_type(filename))
