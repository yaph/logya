import unittest

from logya.docreader import DocReader


class TestDocReader(unittest.TestCase):

    def setUp(self):
        self.reader = DocReader('./fixtures/')

    def test_markup_type(self):
        self.assertEqual('markdown', self.reader.markup_type('test.md'))
        self.assertEqual('markdown', self.reader.markup_type('test.markdown'))
        self.assertEqual('html', self.reader.markup_type('test.html'))
        self.assertEqual('html', self.reader.markup_type('test.htm'))
        self.assertIsNone(self.reader.markup_type('test.js'))
