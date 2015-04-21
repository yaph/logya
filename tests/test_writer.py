import unittest
from logya.writer import FileWriter


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        self.filewriter = FileWriter()

    def test_canonical_filename(self):
        testdata = [{'input': 'recipes',
                     'expected': 'recipes/index.html'},
                    {'input': '/recipes/',
                     'expected': 'recipes/index.html'},
                    {'input': '/recipes',
                     'expected': 'recipes/index.html'},
                    {'input': '/recipes/veggy',
                     'expected': 'recipes/veggy/index.html'},
                    {'input': '/recipes/veggy/index.html',
                     'expected': 'recipes/veggy/index.html'},
                    {'input': '/recipes/veggy.html',
                     'expected': 'recipes/veggy.html'}]

        for paths in testdata:
            self.assertEqual(
                self.filewriter.canonical_filename(paths['input']),
                paths['expected'])
