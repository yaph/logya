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
            ('/dotd/2015/03/22/', ['dotd', '2015', '03'])]

        for test in tests:
            self.assertEqual(test[1], path.list_dirs_from_url(test[0]))
