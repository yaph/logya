from __init__ import TestLogya

from logya.ext import ExtensionLoader

class TestExtensions(TestLogya):

    def setUp(self):
        self.extension_loader = ExtensionLoader()

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
