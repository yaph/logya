import unittest

from logya import path


class TestPath(unittest.TestCase):

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

    def test_list_dirs_from_url(self):
        tests = [
            ('/index.html', []),
            ('/video/crouton-explained-hp-chromebook-11/', ['video']),
            ('__index__/index/', ['__index__']),
            ('/tags/video-tutorial/index.html', ['tags', 'video-tutorial']),
            ('/qotd/2015/03/22/', ['qotd', '2015', '03'])]

        for test in tests:
            self.assertEqual(test[1], path.list_dirs_from_url(test[0]))

    def test_slugify(self):
        tests = [
            ('FOSDEM', 'fosdem'),
            ('Video Demonstration', 'video-demonstration'),
            ('Chrome OS', 'chrome-os')]

        for test in tests:
            self.assertEqual(test[1], path.slugify(test[0]))

    def test_url_from_filename(self):
        basedir = '/www/linux-netbook.com/content'
        tests = [
            ('/www/linux-netbook.com/content/compare/laptops.md',
             '/compare/laptops/'),
            ('/www/linux-netbook.com/content/review/hp-mini.html',
             '/review/hp-mini/')]
        for test in tests:
            self.assertEqual(
                test[1], path.url_from_filename(test[0], basedir=basedir))
