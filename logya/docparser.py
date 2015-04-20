# -*- coding: utf-8 -*-
import os
import markdown

from datetime import datetime
from logya.compat import file_open as open

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(filename):
    """Parse document and return a dictionary of header fields and body."""

    stat = os.stat(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    if not content:
        return

    # Extract YAML header and body.
    pos1 = content.index('---')
    pos2 = content.index('---', pos1 + 1)
    header = content[pos1:pos2].strip()
    body = content[pos2 + 3:].strip()

    # Parse body if not HTML/XML.
    fext = os.path.splitext(filename)[1]
    if '.md' == fext or '.markdown' == fext:
        body = markdown.markdown(body.decode('utf-8'))

    parsed = load(header, Loader=Loader)
    parsed['body'] = body

    # Use file modification time for created and updated properties, if not
    # set in document itself.
    modified = datetime.fromtimestamp(stat.st_mtime)
    if 'created' not in parsed:
        parsed['created'] = modified
    if 'updated' not in parsed:
        parsed['updated'] = modified

    return parsed
