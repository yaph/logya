# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
import subprocess
import unittest

class TestCommand(unittest.TestCase):
    def setUp(self):
        self.dir_site = tempfile.mkdtemp()
        os.chdir(self.dir_site)
        subprocess.call(['logya', 'create', 'logyatest'])

    def tearDown(self):
        #shutil.rmtree(self.dir_site, True)
        pass

    def test_create(self):
        self.assertEqual(1, 1)

    def test_generate(self):
        pass


if __name__ == '__main__':
    unittest.main()
