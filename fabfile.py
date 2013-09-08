# -*- coding: utf-8 -*-
from fabric.api import local, lcd


def release():
    local('nosetests')
    local('python setup.py sdist upload')


def git():
    local('git add . && git commit -a')
    local('git push')


def reinstall():
    local('pip uninstall -y logya')
    local('python setup.py install')


def test():
    local('rm -rf t')
    local('`which logya` create t')
    with lcd('t'):
        local('`which logya` gen')


def rt():
    reinstall()
    test()