import os
import sys
import unittest
cwd = sys.path[0]
dir_app = os.path.join(os.path.dirname(cwd), 'geeklog')
sys.path.append(dir_app)

from geeklog import Geeklog
from ext import ExtensionLoader

class TestGeeklog(unittest.TestCase):

    def setUp(self):
        self.geeklog = Geeklog()
        self.geeklog.set_dir_current(os.path.join(dir_app, 'sites', 'geeksta'))
        self.geeklog.init_env()
        self.extension_loader = ExtensionLoader()

class TestExtensionDirectory(TestGeeklog):

    def test_disqus(self):
        expected = 'geeklog/ext/disqus'
        for e in self.extension_loader.get_by_type('doc'):
            if 'disqus' == e.get_module_name():
                self.assertTrue(e.get_directory().endswith(expected))

if __name__ == '__main__':
    unittest.main()
