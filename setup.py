#!/usr/bin/env python
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from logya import __version__

setup(
    name='logya',
    version=__version__,
    description='Logya: easy to use and flexible static site generator.',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
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
    install_requires=Path('requirements.txt').read_text().split('\n'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
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
    tests_require=['pytest', 'tox'],
)
