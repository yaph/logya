import pytest

import logya.core
import logya.template

# Test the functions called in templates.
env_globals = logya.template.env.globals
env_filters = logya.template.env.filters

@pytest.fixture
def L():
    L = logya.core.Logya(dir_site='logya/sites/docs/')
    L.build()
    return L


def test_alpha_index(L):
    docs = [val['doc'] for val in L.doc_index.values()]
    ai = env_filters['alpha_index'](docs)
    assert len(docs) >= len(ai)
    assert 'l' in ai  # Logya Static Site Generator Documentation
    assert 'x' in ai  # XML Sitemap


def test_attr_contains(L):
    docs = [val['doc'] for val in L.doc_index.values()]
    assert len(docs) == len(env_filters['attr_contains'](docs, 'url', '/'))
    assert env_filters['attr_contains'](docs, 'template', '.html')
    assert env_filters['attr_contains'](docs, 'template', '.xml')


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


def test_filesource_lines():
    text = env_globals['filesource']('content/rss.xml', lines=1)
    assert text == '---'


def test_filesource_image():
    text = env_globals['filesource']('static/img/logya-small.png')
    assert text is None


def test_filesource_raw():
    assert '&lt;' in env_globals['filesource']('templates/base.html')
    assert '<' in env_globals['filesource']('templates/base.html', raw=True)
