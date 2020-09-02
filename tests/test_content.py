#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logya.content import read


def test_read_markdown():
    doc = read('tests/fixtures/site/content/markdown.md')
    assert isinstance(doc, dict)
    assert '/test/markdown/' == doc['url']
