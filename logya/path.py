# -*- coding: utf-8 -*-
# Wrappers for functions from os.path.
import os
import re

re_url_replace = re.compile(r'[\/\s_]+')


class PathResourceError(Exception):
    pass


def join(basedir, *args, **kwargs):
    """Get joined name relative to basedir for file or path name.

    Raises an exception if resource is required and doesn't exist.
    """

    path = os.path.join(basedir, *args)
    if kwargs.get('required') and not os.path.exists(path):
        raise PathResourceError(
            'Resource at path {} does not exist.'.format(path))
    return path


def list_dirs_from_url(url):
    """Returns a list of directories from given url.

    The last directory is omitted as it contains an index.html file
    containing the content of the corresponding document."""

    return [d for d in url.strip('/').split('/') if d][:-1]


def slugify(path):
    return re.sub(re_url_replace, '-', path).lower()


def url_from_filename(filename, basedir=None):
    """Creates a URL to be used in docs from basedir and filename."""

    ext = os.path.splitext(filename)[1]
    if ext:
        filename = filename.replace(ext, '/')

    if basedir:
        filename = filename.replace(basedir, '')

    return filename
