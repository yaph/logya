# -*- coding: utf-8 -*-
# Wrappers for functions from os.path.
import os


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
