# -*- coding: utf-8 -*-
import logya.util


site_root = 'tests/fixtures/site/'
site_paths = logya.util.paths(site_root)


def test_encode_content():
    text = logya.util.encode_content({}, '')
    assert 2 == text.count('---\n')


def test_slugify():
    for value, expected in [
        ('ac/dc', 'ac-dc'),
        ('AC/DC', 'AC-DC'),
        ('Gómez', 'Gómez'),
        ('Rock \'n Roll', 'Rock-n-Roll'),
        ('Rock \'n\' Roll', 'Rock-n-Roll'),
        ('multiple   spaces', 'multiple-spaces'),
        ('c♯dim', 'c♯dim'),
        ('_85QotzbzHY', '_85QotzbzHY'),
        ('dot.dot', 'dot.dot'),
    ]:
        assert logya.util.slugify(value) == expected


def test_paths():
    assert site_paths.public.as_posix() == site_root + 'public'