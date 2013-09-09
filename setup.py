#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from logya import __version__

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='logya',
    version=__version__,
    description='Logya: easy to use and flexible static Web site generator.',
    long_description=readme,
    url='http://yaph.github.com/logya/',
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='code@ramiro.org',
    keywords=['Website Generator'],
    license=license,
    packages=['logya'],
    include_package_data=True,
    exclude_package_data={'': ['*.pyc']},
    install_requires=required,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
    entry_points={
        'console_scripts': [
            'logya = logya.main:main'
        ]
    }
)