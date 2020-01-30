# -*- coding: utf-8 -*-
from datetime import datetime
from os import walk
from pathlib import Path

from logya import allowed_exts
from logya.util import slugify

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def add_collections(site_index, settings):
    if 'collections' not in settings:
        return

    collections = settings['collections']
    collection_names = set(collections.keys())
    collection_index = {}

    for doc_url, content in site_index.items():
        doc = content['doc']
        for attr in set(doc.keys()) & collection_names:
            values = doc[attr]
            for value in values:
                index_url = f'/{collections[attr]["path"]}/{slugify(value.lower())}/'
                if index_url in site_index:
                    print(f'Index at {index_url} will not be created, because a content document exists.')
                    continue
                if index_url in collection_index:
                    collection_index[index_url]['docs'].append(doc)
                else:
                    collection_index[index_url] = {
                        'docs': [doc],
                        'title': value,
                        'path': collections[attr]['path'],
                        'template': collections[attr].get('template', settings['content']['index']['template']),
                        'url': index_url
                    }

    site_index.update(collection_index)


def content_type(path):
    if path.suffix in ['.html', '.htm']:
        return 'html'
    if path.suffix in ['.md', '.markdown']:
        return 'markdown'


def create_url(path):
    # path/to/name.md -> /path/to/name/
    # path/to/index.md -> /path/to/
    if 'index' == path.stem:
        path = Path(path.parent)
    else:
        path = Path(path.parent, path.stem)

    return f'/{"/".join(slugify(p.lower()) for p in path.parts)}/'


def parse(content, content_type=None):
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body and load header into dict.
    pos1 = content.index('---')
    pos2 = content.index('---', pos1 + 1)
    header = content[pos1:pos2].strip()
    body = content[pos2 + 3:].strip()
    parsed = load(header, Loader=Loader)
    parsed['body'] = body
    return parsed


def read(path):
    content = path.read_text().strip()
    try:
        doc = parse(content, content_type=content_type(path))
    except Exception as err:
        print(f'Error parsing: {path}\n{err}')
        return

    # Use file modification time for created and updated attributes if not set in document.
    modified = datetime.fromtimestamp(path.stat().st_mtime)
    for attr in ['created', 'updated']:
        if attr not in doc:
            doc[attr] = modified

    return doc


def read_all(dir_content):
    # Index mapping URLs to content objects
    index = {}

    for root, _, files in walk(dir_content):
        for f in files:
            path = Path(root, f)
            if path.suffix.lstrip('.') not in allowed_exts:
                continue

            doc = read(path)
            if not doc:
                continue

            # URLs set in the document are prioritized and left unchanged.
            doc['url'] = doc.get('url', create_url(path.relative_to(dir_content)))

            index[doc['url']] = {
                'doc': doc,
                'path': path
            }

    return index


def write(filename, doc):
    # Parse body if not HTML/XML.
    # if body and content_type == 'markdown':
    #     body = markdown.markdown(
    #         body,
    #         extensions=[
    #             'markdown.extensions.attr_list',
    #             'markdown.extensions.def_list',
    #             'markdown.extensions.fenced_code'
    #         ])
    pass


def write_collection(path, content, template, settings):
    """Write an auto-generated index.html file."""

    template.vars['docs'] = content['docs']
    template.vars['title'] = content['title']
    template.vars['canonical'] = settings['site']['base_url'] + content['url']

    page = template.env.get_template(content['template'])
    path.parent.mkdir(exist_ok=True)
    path.write_text(page.render(template.vars))
