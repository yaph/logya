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
