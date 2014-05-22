# -*- coding: utf-8 -*-
from fabric.api import local, lcd


def build_docs():
    local('python setup.py build_sphinx')


def docs():
    build_docs()
    local('python setup.py upload_sphinx')


def reinstall():
    local('pip uninstall -y logya')
    local('python setup.py install')


def test():
    local('nosetests tests')
    local('rm -rf t')
    local('`which logya` create t')
    with lcd('t'):
        local('`which logya` gen')


def release():
    test()
    local('python setup.py sdist upload')


def rt():
    reinstall()
    test()