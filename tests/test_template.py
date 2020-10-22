#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

import logya.core
import logya.template

# Test the functions called in templates.
env_globals = logya.template.env.globals

@pytest.fixture
def L():
    L = logya.core.Logya(dir_site='logya/sites/docs/')
    L.build()
    return L


def test_get_docs(L):
    doc_count = len(L.doc_index)
    assert doc_count > 1
    assert len(env_globals['get_docs']()) == doc_count
    assert len(env_globals['get_docs']('')) == doc_count
    assert len(env_globals['get_docs']('/')) == doc_count
    assert len(env_globals['get_docs'](url='')) == doc_count
    assert len(env_globals['get_docs'](url='/')) == doc_count


def test_filesource():
    text = env_globals['filesource']('site.yaml')
    assert 'base_url:' in text
    assert 'collections:' in text


def test_filesource_image():
    text = env_globals['filesource']('static/img/logya.png')
    assert text is None