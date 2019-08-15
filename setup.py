#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from logya import __version__

# Use io.open to be able to set encoding to utf-8.
with io.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

with io.open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='logya',
    version=__version__,
    description='Logya: easy to use and flexible static Web site generator.',
    long_description=readme,
    url='https://ramiro.org/logya/',
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    maintainer='Ramiro Gómez',
    maintainer_email='code@ramiro.org',
    keywords=['Website Generator'],
    license='MIT',
    packages=['logya'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    exclude_package_data={'': ['*.pyc']},
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    entry_points={
        'console_scripts': [
            'logya = logya.main:main'
        ]
    },
    test_suite='tests',
    tests_require=['tox'],
)
