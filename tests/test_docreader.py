import unittest

from logya.docreader import content_type


class TestDocReader(unittest.TestCase):

    def test_content_type(self):
        self.assertEqual('markdown', content_type('test.md'))
        self.assertEqual('markdown', content_type('test.markdown'))
        self.assertEqual('html', content_type('test.html'))
        self.assertEqual('html', content_type('test.htm'))
        self.assertIsNone(content_type('test.js'))
