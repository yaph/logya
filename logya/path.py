# -*- coding: utf-8 -*-
# Wrappers for functions from os.path.
import os
import re

from logya import allowed_exts

re_url_replace = re.compile(r'[\/\s_]+')


class PathResourceError(Exception):
    pass


def canonical_filename(name):
    """Get file name from given path or file.

    If name is not recognized as a file name a /index.html is added. To be
    recognized as a file name it must end with an allowed extension.
    Leading slashes are stripped off.
    """

    # Paths for generated indexes do not start with a slash.
    if not name.startswith('/'):
        name = '/' + name

    # Only allowed extension will be written to a file, otherwise a
    # directory with the name is created and content written to index.html.
    ext = os.path.splitext(name)[1]
    if not ext or ext.lstrip('.') not in allowed_exts:
        name = os.path.join(name, 'index.html')

    return name.lstrip('/')


def join(basedir, *args, **kwargs):
    """Get joined name relative to basedir for file or path name.

    Raises an exception if resource is required and doesn't exist.
    """

    path = os.path.join(basedir, *args)
    if kwargs.get('required') and not os.path.exists(path):
        raise PathResourceError(
            'Resource at path {} does not exist.'.format(path))
    return path


def parent_dirs(url):
    """Returns a list of parent directories for url without the root /."""

    return url.strip('/').split('/')[:-1]


def parent_paths(dirs):
    """Returns a list of absolute parent directory paths for given dirs."""

    return ('/'.join(dirs[:i + 1]) for i, _ in enumerate(dirs))


def slugify(path):
    return re.sub(re_url_replace, '-', path.strip()).lower()


def target_file(basedir, url):
    """Determine the absolute filename to create and return it.

    If a URL points to a directory 'index.html' will be appended.
    """

    filename = canonical_filename(url)
    return os.path.join(basedir, filename)


def url_from_filename(filename, basedir=None):
    """Creates a URL to be used in docs from basedir and filename."""

    ext = os.path.splitext(filename)[1]
    if ext:
        filename = filename.replace(ext, '/')

    if basedir:
        filename = filename.replace(basedir, '')

    return filename
