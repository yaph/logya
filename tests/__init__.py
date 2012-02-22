#!/usr/bin/env python
import os
import sys
import unittest
import test_commands
import test_extensions
import test_writer

cwd = sys.path[0]
dir_app = os.path.join(cwd, 'logya')
sys.path.insert(0, dir_app)

from logya import Logya


def run():
    """Run logya tests."""

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_commands)
    suite.addTests(loader.loadTestsFromModule(test_extensions))
    suite.addTests(loader.loadTestsFromModule(test_writer))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestLogya(unittest.TestCase):
    """Base class for logya tests."""

    def setUp(self):
        """Common set up tasks."""

        os.chdir(os.path.join(dir_app, 'sites', 'docs'))
        self.logya = Logya()
        self.logya.init_env()

    #~ @unittest.skip("todo")
    #~ def test_update_indexes(self):
        #~ """Provide paths to test correct index associations."""
        #~ pass

if __name__ == "__main__":
    run()
