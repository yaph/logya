# -*- coding: utf-8 -*-
import unittest

class TestCommand(unittest.TestCase):
    print 1

class TestCreate(TestCommand):
    pass

class TestGenerate(TestCommand):
    pass
