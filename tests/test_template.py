#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logya.core
import logya.template

L = logya.core.Logya(dir_site='logya/sites/base/')
L.build()

# Test the functions called in templates.
env_globals = logya.template.env.globals


def test_get_docs():
    doc_count = len(L.doc_index)
    assert doc_count > 1
    assert len(env_globals['get_docs']()) == doc_count
    assert len(env_globals['get_docs']('')) == doc_count
    assert len(env_globals['get_docs']('/')) == doc_count
    assert len(env_globals['get_docs'](url='')) == doc_count
    assert len(env_globals['get_docs'](url='/')) == doc_count


def test_filesource():
    text = env_globals['filesource']('site.yaml')
    assert 'base_url: http://localhost:8080' in text
    assert 'collections:' in text