#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logya.content
import tests.fixtures.docs as docs

from pathlib import Path

from logya.util import paths


site_root = 'tests/fixtures/site/'
site_paths = paths(site_root)


def test_content_type():
    for value, expected in [
        ('test.markdown', 'markdown'),
        ('test.md', 'markdown'),
        ('test.htm', 'html'),
        ('test.html', 'html'),
        ('test.js', None),
    ]:
        assert logya.content.content_type(Path(value)) == expected


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


def test_parse_separator():
    doc = logya.content.read(Path(site_root, 'content', 'separator.md'), site_paths)
    assert '---' in doc['body']
    assert '---' in doc['title']


# def test_parse_markdown_links():
#     doc = logya.content.parse(docs.markdown_link, content_type='markdown')
#     assert '<a href="/url/">Link</a>' in doc['body']


# def test_parse_markdown_attrs():
#     doc = logya.content.parse(docs.markdown_attrs, content_type='markdown')
#     assert '<a class="foo bar" href="/url/" title="Some title!">Link with attributes</a>' in doc['body']
