#http://docs.python.org/library/unittest.html#organizing-test-code
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

    def test_extension_directory(self):
        expected = 'logya/ext/disqus'
        for e in self.extension_loader.get_by_type('doc'):
            if 'disqus' == e.get_module_name():
                self.assertTrue(e.get_directory().endswith(expected))

    # TODO
    def test_update_indexes(self):
        """Provide paths to test correct index associations."""
        pass


if __name__ == '__main__':
    unittest.main()
