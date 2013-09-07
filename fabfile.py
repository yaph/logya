# -*- coding: utf-8 -*-
from fabric.api import local


def release():
    local('nosetests')
    local('python setup.py sdist upload')


def git():
    local('git add . && git commit -a')
    local('git push')


def reinstall():
    local('pip uninstall logya')
    local('python setup.py logya')