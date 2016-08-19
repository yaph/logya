import unittest

from logya import path


class TestPath(unittest.TestCase):

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
                path.canonical_filename(paths['input']),
                paths['expected'])

    def test_join(self):
        self.assertEqual(
            'dir/file.ext', path.join('dir', 'file.ext'))
        self.assertEqual(
            'dir/subdir/file.ext', path.join('dir', 'subdir', 'file.ext'))

    def test_join_required_exists(self):
        self.assertEqual('tests', path.join('tests', required=True))

    def test_join_required_not_exists(self):
        self.assertRaises(path.PathResourceError,
                          path.join,
                          *('dir', 'file.ext'),
                          required=True)

    def test_parent_dirs(self):
        tests = [
            ('/index.html', []),
            ('/video/crouton-explained-hp-chromebook-11/', ['video']),
            ('__index__/index/', ['__index__']),
            ('/tags/video-tutorial/index.html', ['tags', 'video-tutorial']),
            ('/qotd/2015/03/22/', ['qotd', '2015', '03'])]

        for test_input, expected in tests:
            self.assertEqual(expected, path.parent_dirs(test_input))

    def test_parent_paths(self):
        tests = [
            (['map'], ['map']),
            (['map', 'spain', 'choropleth'], ['map', 'map/spain', 'map/spain/choropleth'])
        ]

        for test_input, expected in tests:
            self.assertEqual(expected, list(path.parent_paths(test_input)))

    def test_slugify(self):
        tests = [
            ('FOSDEM', 'fosdem'),
            ('Video Demonstration', 'video-demonstration'),
            ('Chrome OS', 'chrome-os')]

        for test_input, expected in tests:
            self.assertEqual(expected, path.slugify(test_input))

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
                path.target_file(t['basedir'], t['url']))

    def test_url_from_filename(self):
        basedir = '/www/linux-netbook.com/content'
        tests = [
            ('/www/linux-netbook.com/content/compare/laptops.md',
             '/compare/laptops/'),
            ('/www/linux-netbook.com/content/review/hp-mini.html',
             '/review/hp-mini/')]

        for test_input, expected in tests:
            self.assertEqual(
                expected, path.url_from_filename(test_input, basedir=basedir))
