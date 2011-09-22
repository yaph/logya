#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://packages.python.org/distribute/setuptools.html#declaring-dependencies

from setuptools import setup
from geeklog import __version__

setup(
    name='geeklog',
    version=__version__,
    description='TODO',
    long_description=open('README.markdown').read(),
    url='TODO',
    download_url='TODO-geeklog-%s.tar.gz' % __version__,
    author='Ramiro Gómez',
    author_email='web@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='web@ramiro.org',
    keywords=['Website Generator'],
    license='MIT',
    packages = find_packages(),
    test_suite='tests.all_tests',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python'],
    install_requires=['distribute', 'jinja2'],
    entry_points = {
        'console_scripts': [
            'geeklog = geeklog.main:main'
        ]
    }
)
