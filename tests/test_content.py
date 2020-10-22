#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

import logya.content

from pathlib import Path

from logya.util import paths


markdown_extensions = ['attr_list', 'def_list', 'fenced_code', 'toc']
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


def test_filepath():
    for value, expected in [
        ('chord', 'public/chord/index.html'),
        ('/chord', 'public/chord/index.html'),
        ('/chord/', 'public/chord/index.html'),
        ('chord/am', 'public/chord/am/index.html'),
        ('/chord/am', 'public/chord/am/index.html'),
        ('/chord/am/', 'public/chord/am/index.html'),
        ('/artist/ben-e.-king/', 'public/artist/ben-e.-king/index.html'),
    ]:
        assert logya.content.filepath(site_paths.public, value).as_posix().endswith(expected)


def test_parse_empty_body():
    path_md = Path(site_root, 'content', 'empty_body.md')
    doc = logya.content.read(path_md, path_md.relative_to(site_paths.content), markdown_extensions)
    assert '' == doc['body']


def test_read_auto_url():
    path_md = Path(site_root, 'content', 'separator.md')
    doc = logya.content.read(path_md, path_md.relative_to(site_paths.content), markdown_extensions)
    assert '/separator/' == doc['url']


def test_read_missing_file():
    path_md = Path(site_root, 'content', 'missing.md')
    with pytest.raises(FileNotFoundError) as err:
        doc = logya.content.read(path_md, path_md.relative_to(site_paths.content), markdown_extensions)


def test_read_markdown():
    path_md = Path(site_root, 'content', 'markdown.md')
    doc = logya.content.read(path_md, path_md.relative_to(site_paths.content), markdown_extensions)
    assert '<a href="/url/">Link</a>' in doc['body']
    assert '<a class="foo bar" href="/url/" title="Some title!">Link with attributes</a>' in doc['body']