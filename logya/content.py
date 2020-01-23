# -*- coding: utf-8 -*-
from pathlib import Path

from logya.docparser import parse


def content_type(path):
    if path.suffix in ['.html', '.htm']:
        return 'html'
    if path.suffix in ['.md', '.markdown']:
        return 'markdown'


def read(filename):
    path = Path(filename)
    content = path.read_text().strip()
    try:
        return parse(content, content_type=content_type(path))
    except Exception as err:
        print(f'Error parsing: {filename}\n{err}')
    # TODO add url, created and updated attrs if not set


def write(filename, doc):
    pass
