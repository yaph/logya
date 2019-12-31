# -*- coding: utf-8 -*-
import markdown

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse(content, content_type=None):
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body and load header into dict.
    pos1 = content.index('---')
    pos2 = content.index('---', pos1 + 1)
    header = content[pos1:pos2].strip()
    body = content[pos2 + 3:].strip()
    parsed = load(header, Loader=Loader)

    # Parse body if not HTML/XML.
    if body and content_type == 'markdown':
        body = markdown.markdown(
            body,
            extensions=[
                'markdown.extensions.attr_list',
                'markdown.extensions.def_list',
                'markdown.extensions.fenced_code'
            ])

    parsed['body'] = body
    return parsed
