import unittest
from logya.writer import FileWriter


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        self.filewriter = FileWriter()
