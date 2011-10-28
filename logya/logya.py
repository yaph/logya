# -*- coding: utf-8 -*-
import os
import sys
import shutil
import config
from template import Template

class Logya(object):
    """Class with main logic for creating, building and serving a static Web site."""

    def __init__(self, **kwargs):

        if kwargs.has_key('verbose') and kwargs['verbose']:
            self.verbose = True
        else:
            self.verbose = False

        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

        # a dictionary of indexes with parsed documents
        self.indexes = {}

        self.dir_src = sys.path[0]
        self.dir_current = os.getcwd()

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print msg

    def set_dir_current(self, dir_current):
        """Called from tests."""

        self.dir_current = dir_current

    def test_and_get_path(self, name):
        """Test whether resource exists at path relative to current directory and return its full path."""

        path = os.path.join(self.dir_current, name)
        if not os.path.exists(path):
            raise Exception('Path "%s" does not exist.' % path)
        return path

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        file_conf = self.test_and_get_path('site.cfg')
        self.config = config.get(file_conf)

        self.dir_content = self.test_and_get_path('content')
        self.dir_static = self.test_and_get_path('static')

        dir_templates = self.test_and_get_path('templates')
        self.template = Template(dir_templates)
        self.template.add_var('base_path', self.config.get('site', 'base_path'))

        self.dir_dst = os.path.join(self.dir_current, 'deploy')