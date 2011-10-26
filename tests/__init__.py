import os
import sys
import unittest
cwd = sys.path[0]
dir_app = os.path.join(os.path.dirname(cwd), 'logya')
sys.path.append(dir_app)

from logya import Logya
from ext import ExtensionLoader

class TestLogya(unittest.TestCase):

    def setUp(self):
        self.logya = Logya()
        self.logya.set_dir_current(os.path.join(dir_app, 'sites', 'geeksta'))
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

if __name__ == '__main__':
    unittest.main()
