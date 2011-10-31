#http://docs.python.org/library/unittest.html#test-discovery
import os
import sys
import unittest
cwd = sys.path[0]
dir_app = os.path.join(os.path.dirname(cwd), 'logya')
sys.path.append(dir_app)

from logya.logya import Logya
from logya.ext import ExtensionLoader

class TestLogya(unittest.TestCase):

    def setUp(self):
        self.logya = Logya()
        self.logya.set_dir_current(os.path.join(dir_app, 'sites', 'docs'))
        self.logya.init_env()
        self.extension_loader = ExtensionLoader()

class TestExtensionDirectory(TestLogya):

    def test_disqus(self):
        expected = 'logya/ext/disqus'
        for e in self.extension_loader.get_by_type('doc'):
            if 'disqus' == e.get_module_name():
                self.assertTrue(e.get_directory().endswith(expected))

# TODO
class TestUpdateIndexes(TestLogya):
    """Provide paths to test correct index associations."""
    pass

# used for running all tests from single commmand
class All(unittest.TestSuite):

    def __init__(self):
        self.addTest(TestExtensionDirectory())

if __name__ == '__main__':
    unittest.main()
