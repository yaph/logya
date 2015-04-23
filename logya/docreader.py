# -*- coding: utf-8 -*-
import io
import os

from datetime import datetime

from logya import allowed_exts, path
from logya.docparser import parse


def content_type(filename):
    ctype = None
    ext = os.path.splitext(filename)[1]
    if ext in ['.html', '.htm']:
        ctype = 'html'
    elif ext in ['.md', '.markdown']:
        ctype = 'markdown'
    return ctype


def read(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()


def list_docs(dir_base):
    """Recurse through directory to add documents to process."""
    docs = []
    for root, dirs, files in os.walk(dir_base):
        docs.extend([
            os.path.join(root, f) for f in files
            if os.path.splitext(f)[1].strip('.') in allowed_exts])
    return docs


class DocReader:
    """A class for reading content documents."""

    def __init__(self, basedir):
        self.basedir = basedir
        self.files = list_docs(basedir)

    @property
    def parsed(self):
        """Generator that reads all docs from base directory and returns parsed
        content."""

        for filename in self.files:
            stat = os.stat(filename)
            content = read(filename)
            if not content:
                continue

            modified = datetime.fromtimestamp(stat.st_mtime)
            parsed = parse(content, content_type=content_type(filename))

            # Use file modification time for created and updated properties,
            # if not set in document itself.
            parsed['created'] = parsed.get('created', modified)
            parsed['updated'] = parsed.get('updated', modified)

            # Set url from filename if not in set in parsed document.
            if 'url' not in parsed:
                parsed['url'] = path.url_from_filename(
                    filename, basedir=self.basedir)

            yield parsed
