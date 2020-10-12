# -*- coding: utf-8 -*-
import logya.util


site_root = 'tests/fixtures/site/'
site_paths = logya.util.paths(site_root)


def test_filepath():
    for value, expected in [
        ('chord', 'public/chord/index.html'),
        ('/chord', 'public/chord/index.html'),
        ('/chord/', 'public/chord/index.html'),
        ('chord/am', 'public/chord/am/index.html'),
        ('/chord/am', 'public/chord/am/index.html'),
        ('/chord/am/', 'public/chord/am/index.html'),
    ]:
        assert logya.util.filepath(site_paths.public, value).as_posix().endswith(expected)


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