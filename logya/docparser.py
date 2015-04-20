# -*- coding: utf-8 -*-
import markdown

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(content, modified=None, markup=None):
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body.
    pos1 = content.index('---')
    pos2 = content.index('---', pos1 + 1)
    header = content[pos1:pos2].strip()
    body = content[pos2 + 3:].strip()

    # Parse body if not HTML/XML.
    if markup == 'markdown':
        body = markdown.markdown(body.decode('utf-8'))

    parsed = load(header, Loader=Loader)
    parsed['body'] = body

    # Use file modification time for created and updated properties, if not
    # set in document itself.
    if 'created' not in parsed:
        parsed['created'] = modified
    if 'updated' not in parsed:
        parsed['updated'] = modified

    return parsed
