import unittest

from logya.docreader import DocReader


class TestDocReader(unittest.TestCase):

    def setUp(self):
        self.reader = DocReader('./fixtures/')

    def test_content_type(self):
        self.assertEqual('markdown', self.reader.content_type('test.md'))
        self.assertEqual('markdown', self.reader.content_type('test.markdown'))
        self.assertEqual('html', self.reader.content_type('test.html'))
        self.assertEqual('html', self.reader.content_type('test.htm'))
        self.assertIsNone(self.reader.content_type('test.js'))
