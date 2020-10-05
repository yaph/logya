# -*- coding: utf-8 -*-
from logya.content import read_all
from logya.template import init_env
from logya.util import load_yaml, paths


class Logya:
    """Object to store data such as site index and settings."""

    def __init__(self, options):
        """Set required logya object properties."""

        self.verbose = getattr(options, 'verbose', False)
        self.paths = paths(dir_site=getattr(options, 'dir_site', None))
        self.settings = load_yaml(self.paths.root.joinpath('site.yaml').read_text())

        # Initialize template env and globel variables.
        init_env(self.settings, self.index)
        self.template_vars = self.settings['site']

    def build_index(self):
        """Build index of documents and collections."""

        self.index = read_all(self.settings)

    def write_index(self):
        pass

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)
