import pytest

import logya.core


@pytest.fixture
def L():
    return logya.core.Logya(dir_site='logya/sites/base/')


def test_build(L):
    L.build()

    assert '/' in L.doc_index
    assert '/404/' in L.doc_index
