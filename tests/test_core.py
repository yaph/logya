#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logya.core


L = logya.core.Logya(dir_site='logya/sites/base/')


def test_build():
    L.build()

    assert '/' in L.doc_index
    assert '/404/' in L.doc_index