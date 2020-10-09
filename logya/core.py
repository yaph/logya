# -*- coding: utf-8 -*-
from os import walk
from pathlib import Path

from logya.content import read, process_extensions
from logya.template import init_env
from logya.util import load_yaml, paths, slugify


class Logya:
    """Object to store data such as site index and settings."""

    def __init__(self, options):
        """Set required logya object properties."""

        self.verbose = getattr(options, 'verbose', False)
        self.paths = paths(dir_site=getattr(options, 'dir_site', None))
        self.settings = load_yaml(self.paths.root.joinpath('site.yaml').read_text())

        # Initialize index and collections so scripts can generate indexed content before build.
        self.index = {}
        self.collections = self.settings.get('collections', {})
        for name, coll in self.collections.items():
            coll['index'] = {}

    def build(self):
        """Read content and initialize template environment."""

        self.read_content()

        # Initialize template env.
        init_env(self.settings, self.index)

    def info(self, msg: str):
        """Print message if in verbose mode."""

        if self.verbose:
            print(msg)

    def read_content(self):
        """Read content and update index and collections.

        Previously indexed content can exist. If a file inside the content directory has the same URL as already indexed
        content, the existing content will be replaced.
        """

        for root, _, files in walk(self.paths.content):
            for f in files:
                path = Path(root, f)
                if path.suffix not in process_extensions:
                    continue
                doc = read(path, path.relative_to(self.paths.content))
                if doc:
                    if self.collections:
                        self.update_collections(doc)
                    self.index[doc['url']] = {'doc': doc, 'path': path}

    def update_collections(self, doc: dict):
        """Update collections index for given doc."""

        # Iterate over copy so attributes can be added.
        for attr, values in doc.copy().items():
            if attr not in self.collections:
                continue
            coll = self.collections[attr]

            # Process unique values.
            for value in set(values):
                url = f'/{coll["path"]}/{slugify(value).lower()}/'

                if url in self.index:
                    print(f'Collection not created because content exists at {url}.')
                    continue

                # Add attribute for creating collection links in templates.
                links = attr + '_links'
                doc[links] = doc.get(links, []) + [(url, value)]

                # Update or create collection index value.
                if url in coll['index']:
                    coll['index'][url]['docs'].append(doc)
                else:
                    coll['index'][url] = {
                        'docs': [doc],
                        'title': value,
                        'template': coll['template'],
                        'url': url
                    }
