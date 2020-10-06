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

        # Initialize index so scripts can generate indexed content before build.
        self.index = {}

    def build(self):
        """Build index of documents and collections."""

        # Previously indexed content can exist. If a document exists in the read directory with the same URL as an
        # already indexed content object, the existing object will be overridden.
        self.index.update(read_all(self.paths, self.settings))

        # Initialize template env.
        init_env(self.settings, self.index)

    def info(self, msg):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)
