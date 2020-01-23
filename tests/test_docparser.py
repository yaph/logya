#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logya.docparser import parse

import tests.fixtures.docs as docs


def test_parse_markdown_link():
    doc = parse(docs.markdown_link, content_type='markdown')
    assert '<a href="/url/">Link</a>' in doc['body']


def test_parse_markdown_attrs():
    doc = parse(docs.markdown_attrs, content_type='markdown')
    assert '<a class="foo bar" href="/url/" title="Some title!">Link with attributes</a>' in doc['body']