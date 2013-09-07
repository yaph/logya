import unittest
from logya import ext


class TestExtensions(unittest.TestCase):

    def setUp(self):
        self.extension_loader = ext.ExtensionLoader()

    def test_extension_directories(self):
        extensions = {
            'disqus': 'logya/ext/disqus',
            'sitemap': 'logya/ext/sitemap',
        }
        # the code below sucks
        for e in self.extension_loader.get_by_type('doc'):
            name = e.get_module_name()
            if 'disqus' == name:
                self.assertTrue(e.get_directory().endswith(extensions[name]))
        for e in self.extension_loader.get_by_type('index'):
            name = e.get_module_name()
            if 'sitemap' == name:
                self.assertTrue(e.get_directory().endswith(extensions[name]))
