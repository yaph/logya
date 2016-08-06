# -*- coding: utf-8 -*-
import unittest

from logya.docparser import parse

import tests.fixtures.docs as docs


class TestDocParser(unittest.TestCase):

    def test_markdown_link(self):
        parsed = parse(docs.markdown_link, content_type='markdown')
        self.assertIn(
            '<a href="/sample/link/">Sample Link</a>', parsed.get('body'))

    def test_markdown_attr_list(self):
        parsed = parse(docs.markdown_attr_list, content_type='markdown')
        self.assertIn(
            '<a class="foo bar" href="/sample/link/" title="Some title!">Sample Link</a>', parsed.get('body'))
