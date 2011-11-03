#!/usr/bin/env python
import os
import sys
import unittest
import test_commands
import test_extensions

cwd = sys.path[0]
dir_app = os.path.join(os.path.dirname(cwd), 'logya', 'logya')
sys.path.append(dir_app)

def run():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_commands)
    suite.addTests(loader.loadTestsFromModule(test_extensions))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

class TestLogya(unittest.TestCase):

    def setUp(self):
        os.chdir(os.path.join(dir_app, 'sites', 'docs'))
        self.logya = Logya()
        self.logya.init_env()

    #~ @unittest.skip("todo")
    #~ def test_update_indexes(self):
        #~ """Provide paths to test correct index associations."""
        #~ pass

if __name__ == "__main__":
    run()
