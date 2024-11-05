from collections import ChainMap
from os import walk
from pathlib import Path
from sys import exit

import yaml

from logya.content import process_extensions, read
from logya.template import init_env
from logya.util import load_yaml, paths, slugify


class Logya:
    """Object to store data such as site index and settings."""

    def __init__(self, dir_site: str = '.', verbose: bool = False) -> None:
        """Set required logya object properties."""

        self.verbose = verbose
        self.paths = paths(dir_site)

        try:
            self.settings = load_yaml(self.paths.root.joinpath('site.yaml').read_text())
        except FileNotFoundError:
            exit('Error: The site configuration file site.yaml was not found.')
        except yaml.scanner.ScannerError:
            exit('Error: The site configuration file site.yaml could not be parsed.')

        # Initialize index and collections so scripts can generate indexed content before build.
        self.doc_index: dict[str, dict] = {}
        self.collections = self.settings.get('collections', {})
        for coll in self.collections.values():
            coll['index'] = {}

        # Simplify access to these settings.
        extensions = self.settings.get('extensions', {})
        self.jinja_extensions = extensions.get('jinja', [])
        self.markdown_extensions = extensions.get('markdown', [])
        self.languages = self.settings.get('languages', {})

    def build(self):
        """Read content and initialize template environment."""

        # Read all recognized files in content directory and create document index and collections.
        self.read_content()

        # Create a ChainMap view from collection indexes.
        self.collection_index = ChainMap(*[coll['index'] for coll in self.collections.values()])

        # Initialize template env.
        init_env(self)

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
                if doc := read(path, path.relative_to(self.paths.content), self.markdown_extensions):
                    if self.collections:
                        self.update_collections(doc)
                    self.doc_index[doc['url']] = {'doc': doc, 'path': path}

    def update_collections(self, doc: dict):
        """Update collections index for given doc."""

        # Iterate over copy so attributes can be added.
        for attr, values in doc.copy().items():
            if attr not in self.collections:
                continue
            coll = self.collections[attr]

            # Process unique values while preserving their order to handle potentially duplicate collection values.
            seen = set()
            for value in values:
                if value in seen:
                    continue
                seen.add(value)

                url = f'/{coll["path"]}/{slugify(value).lower()}/'

                # Prepend language code to URL if language is specified in doc and exists in configuration.
                if 'language' in doc and doc['language'] in self.languages:
                    url = f'/{doc["language"]}{url}'

                if url in self.doc_index:
                    print(f'Collection not created because content exists at {url}.')
                    continue

                # Add attribute for creating collection links in templates.
                links = attr + '_links'
                doc[links] = [*doc.get(links, []), (url, value)]

                # Update or create collection index value.
                if coll_data := coll['index'].get(url):
                    if doc['url'] not in coll_data['doc_urls']:
                        coll_data['doc_urls'].add(doc['url'])
                        coll_data['docs'].append(doc)
                else:
                    coll['index'][url] = {
                        'doc_urls': {doc['url']},
                        'docs': [doc],
                        'title': value,
                        'template': coll['template'],
                        'url': url
                    }
