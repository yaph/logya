# -*- coding: utf-8 -*-
import unittest

from logya.docparser import parse

import tests.fixtures.docs as docs


class TestDocParser(unittest.TestCase):

    def test_markdown_link(self):
        parsed = parse(docs.markdown_link, content_type='markdown')
        self.assertIn(
            '<a href="/sample/link/">Sample Link</a>', parsed.get('body'))
