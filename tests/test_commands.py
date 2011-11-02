# -*- coding: utf-8 -*-
import os
import shutil
import tempfile
import subprocess
import unittest

class TestCommand(unittest.TestCase):
    def setUp(self):
        self.name = 'logyatest'
        self.dir_root = tempfile.mkdtemp()
        self.dir_site = os.path.join(self.dir_root, self.name)
        os.chdir(self.dir_root)

    def tearDown(self):
        #shutil.rmtree(self.dir_root, True)
        pass

    def test_create(self):
        subprocess.call(['logya', 'create', self.name])
        # test whether required directories were created
        for d in ['content', 'templates']:
            self.assertTrue(os.path.exists(os.path.join(self.dir_site, d)))

    #~ def test_generate(self):
        #~ pass


if __name__ == '__main__':
    unittest.main()
