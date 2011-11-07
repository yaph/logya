# -*- coding: utf-8 -*-
import os
from config import Config
from template import Template

class Logya(object):
    """Main logic for creating, building and serving a static site."""

    def __init__(self, **kwargs):
        """Set required logya object properties."""

        if kwargs.has_key('verbose') and kwargs['verbose']:
            self.verbose = True
        else:
            self.verbose = False

        # a dictionary of parsed documents indexed by resource paths
        self.docs_parsed = {}

        # a dictionary of indexes with parsed documents
        self.indexes = {}

        self.dir_current = os.getcwd()

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print msg

    def set_dir_current(self, dir_current):
        """Called from tests."""

        self.dir_current = dir_current

    def get_path(self, name, required=False):
        """Get path relative to current working directory for given name.

        Raises an exception if resource is required and doesn't exist.
        """

        path = os.path.join(self.dir_current, name)
        if required and not os.path.exists(path):
            raise Exception('Resource at path "%s" does not exist.' % path)
        return path

    def init_env(self):
        """Initialize the environment for generating the Web site to deploy.

        This function reads the Web site configuration, sets up the template
        environment and sets object properties.
        """

        self.dir_content = self.get_path('content', required=True)
        self.config = Config(self.get_path('site.cfg', required=True))

        dir_templates = self.get_path('templates', required=True)
        self.template = Template(dir_templates)
        self.template.add_var('base_path', self.config.get('site', 'base_path'))

        # optional directory with static files like style sheets, scripts and images
        self.dir_static = self.get_path('static')

        self.dir_dst = self.get_path('deploy')
