#!/usr/bin/env python
import unittest
import test_commands

def run():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_commands)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

if __name__ == "__main__":
    run()
