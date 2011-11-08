#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from logya import __version__

def get_package_data():
    """Return a list of files in sites dir to include in package."""

    dir_base = os.path.join(os.getcwd(), 'logya')
    dir_sites = os.path.join(dir_base, 'sites')
    sites_files = []
    for root, dirs, files in os.walk(dir_sites):
        sites_files.extend([os.path.join(root, f).replace(dir_base, '').lstrip('/') for f in files])
    return sites_files

setup(
    name='logya',
    version=__version__,
    description='Logya is a static Web site generator written in Python designed to be easy to use and flexible.',
    long_description=open('README.markdown').read(),
    url='http://yaph.github.com/logya/',
    author='Ramiro Gómez',
    author_email='web@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='web@ramiro.org',
    keywords=['Website Generator'],
    license='MIT',
    packages = find_packages(),
    package_data={'logya': get_package_data()},
    #test_suite='tests.all_tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
    install_requires=['distribute', 'jinja2'],
    entry_points = {
        'console_scripts': [
            'logya = logya.main:main'
        ]
    }
)
