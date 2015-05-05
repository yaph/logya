import unittest
from logya import writer


class TestFileWriter(unittest.TestCase):

    def test_target_file(self):
        testdata = ({
            'basedir': '/mysite/deploy',
            'url': '/contact/',
            'expected': '/mysite/deploy/contact/index.html'
        }, {
            'basedir': '/mysite/deploy',
            'url': '/artikel/linguistik/ikon_sprache.html',
            'expected': '/mysite/deploy/artikel/linguistik/ikon_sprache.html'
        }, {
            'basedir': '/mysite/deploy',
            'url': 'tags/code',
            'expected': '/mysite/deploy/tags/code/index.html'
        }, {
            'basedir': '/mysite/deploy',
            'url': 'tags/code/rss.xml',
            'expected': '/mysite/deploy/tags/code/rss.xml'
        })

        for t in testdata:
            self.assertEqual(
                t['expected'],
                writer.target_file(t['basedir'], t['url'], create_dirs=False))
