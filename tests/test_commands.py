# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
import subprocess
import unittest

class TestCommand(unittest.TestCase):

    def _create(self):
        os.chdir(self.dir_root)
        subprocess.call(['logya', 'create', self.name])

    def setUp(self):
        self.name = 'logyatest'
        self.dir_root = tempfile.mkdtemp()
        self.dir_site = os.path.join(self.dir_root, self.name)

    def tearDown(self):
        shutil.rmtree(self.dir_root, True)

    def test_create(self):
        """Test whether required directories were created."""

        self._create()
        for d in ['content', 'templates']:
            self.assertTrue(os.path.exists(os.path.join(self.dir_site, d)))

    def test_generate(self):
        """Test that deploy directory was created."""

        self._create()
        os.chdir(self.dir_site)
        subprocess.call(['logya', 'generate'])

        self.assertTrue(os.path.exists(os.path.join(self.dir_site, 'deploy')))


if __name__ == '__main__':
    unittest.main()
