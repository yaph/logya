#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logya.core
import logya.template


L = logya.core.Logya(dir_site='logya/sites/base/')
L.build()


def test_get_docs():
    doc_count = len(L.doc_index)
    assert len(logya.template._get_docs(L)) == doc_count
    assert len(logya.template._get_docs(L, '')) == doc_count
    assert len(logya.template._get_docs(L, '/')) == doc_count