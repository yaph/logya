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


def iter_docs(basedir):
    """Recurse through directory to add documents to process."""

    return (
        os.path.join(root, f) for root, dirs, files in os.walk(basedir)
        for f in files if os.path.splitext(f)[1].strip('.') in allowed_exts)


def set_date(doc, attribute, default):
    doc[attribute] = doc.get(attribute, default)
    if isinstance(doc[attribute], str):
        try:
            doc[attribute] = datetime.fromisoformat(doc[attribute])
        except ValueError:
            print('Attribute "{}" could not be converted to datetime. URL: {}'.format(attribute, doc))


class DocReader:
    """A class for reading content documents."""

    def __init__(self, basedir):
        self.basedir = basedir

    @property
    def parsed(self):
        """Generator that reads all docs from base directory and returns parsed
        content."""

        for filename in iter_docs(self.basedir):
            try:
                with io.open(filename, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
            except Exception as err:
                print('Error reading file {}\n{}'.format(filename, err))
                continue

            try:
                parsed = parse(content, content_type=content_type(filename))
            except Exception as err:
                print('Error parsing file {}\n{}'.format(filename, err))
                continue

            # Use file modification time for created and updated properties,
            # if not set in document itself.
            modified = datetime.fromtimestamp(os.stat(filename).st_mtime)
            set_date(parsed, 'created', modified)
            set_date(parsed, 'updated', modified)

            # Set url from filename if not set in parsed document.
            if 'url' not in parsed:
                parsed['url'] = path.url_from_filename(filename, basedir=self.basedir)

            yield parsed
