# -*- coding: utf-8 -*-
import markdown

from logya.compat import is3

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(content, modified=None, content_type=None):
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body and load header into dict.
    pos1 = content.index('---')
    pos2 = content.index('---', pos1 + 1)
    header = content[pos1:pos2].strip()
    body = content[pos2 + 3:].strip()
    parsed = load(header, Loader=Loader)

    # Parse body if not HTML/XML.
    if content_type == 'markdown':
        if not is3:
            body = body.decode('utf-8')
        body = markdown.markdown(body)

    parsed['body'] = body
    return parsed
