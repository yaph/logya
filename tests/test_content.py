#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logya.content

from pathlib import Path

from logya.util import paths


site_root = 'tests/fixtures/site/'
site_paths = paths(site_root)


def test_create_url():
    for value, expected in [
        ('index.md', '/'),
        ('sitemap.xml', '/sitemap.xml'),
        ('path/to/index.md', '/path/to/'),
        ('path/to/name.md', '/path/to/name/'),
        ('path/to/my name.md', '/path/to/my-name/'),
        ('path/to/My Name.md', '/path/to/My-Name/'),
    ]:
        assert logya.content.create_url(Path(value)) == expected


def test_read_markdown():
    doc = logya.content.read(Path(site_root, 'content', 'markdown.md'), site_paths)
    assert isinstance(doc, dict)
    assert '/test/markdown/' == doc['url']
