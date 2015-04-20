import unittest

from logya.docparser import parse

import fixtures.docs as docs


class TestDocParser(unittest.TestCase):

    def test_markdown_link(self):
        parsed = parse(docs.markdown_link, markup='markdown')
        self.assertIn(
            '<a href="/sample/link/">Sample Link</a>', parsed.get('body'))
