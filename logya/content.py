# -*- coding: utf-8 -*-
from datetime import datetime
from os import walk
from pathlib import Path

from markdown import markdown

from logya import allowed_exts
from logya.template2 import render
from logya.util import slugify

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


markdown_extensions = [
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.fenced_code']


def add_collections(doc, site_index, collections):
    for attr, values in doc.copy().items():
        if attr not in collections:
            continue
        root = collections[attr]['path']
        for value in values:
            collection_url = f'/{root}/{slugify(value).lower()}/'
            # Add attribute for creating collection links in templates.
            links = attr + '_links'
            doc[links] = doc.get(links, []) + [(collection_url, value)]

            content = site_index.get(collection_url)
            if content:
                if 'doc' in content:
                    print(f'Index at {collection_url} will not be created, because a content document exists.')
                    continue
                # If doc is already in collection update it.
                for idx, collection_doc in enumerate(content['docs']):
                    if doc['url'] == collection_doc['url']:
                        site_index[collection_url]['docs'][idx].update(doc)
                else:
                    content['docs'].append(doc)
            else:
                site_index[collection_url] = {
                    'docs': [doc],
                    'title': value,
                    'path': root,  # FIXME avoid setting path, it is confusing because not a pathlib Path
                    'template': collections[attr]['template'],
                    'url': collection_url
                }


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

    return f'/{"/".join(slugify(p) for p in path.parts)}/'


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


def read(path, settings):
    content = path.read_text().strip()
    try:
        doc = parse(content, content_type=content_type(path))
    except Exception as err:
        print(f'Error parsing: {path}\n{err}')
        return

    # Ensure doc has a title.
    doc['title'] = doc.get('title', path.stem)

    # URLs set in the document are prioritized and left unchanged.
    doc['url'] = doc.get('url', create_url(path.relative_to(settings['paths']['content'])))

    # Use file modification time for created and updated attributes if not set in document.
    modified = datetime.fromtimestamp(path.stat().st_mtime)
    for attr in ['created', 'updated']:
        if attr not in doc:
            doc[attr] = modified

    return doc


def read_all(settings):
    # Index mapping URLs to content objects
    index = {}
    collections = settings.get('collections')

    for root, _, files in walk(settings['paths']['content']):
        for f in files:
            path = Path(root, f)
            if path.suffix.lstrip('.') not in allowed_exts:
                continue
            doc = read(path, settings)
            if doc:
                if collections:
                    add_collections(doc, index, collections)
                index[doc['url']] = {'doc': doc, 'path': path}

    return index


def write_page(path, content, settings):
    # Make all settings in site section available to templates.
    attrs = settings['site']

    # Make doc attributes available to templates.
    attrs.update(content['doc'])

    # Set additional template variables.
    attrs['canonical'] = settings['site']['base_url'] + attrs['url']

    if 'body' in attrs and content_type(content['path']) == 'markdown':
        attrs['body'] = markdown(attrs['body'], extensions=markdown_extensions)

    if 'template' in attrs:
        path.write_text(render(attrs['template'], attrs, pre_render='body'))
    else:
        path.write_text(attrs.get('body', ''))


def write_collection(path, content, settings):
    """Write an auto-generated index.html file."""

    attrs = settings['site']
    attrs['docs'] = content['docs']
    attrs['title'] = content['title']
    attrs['canonical'] = settings['site']['base_url'] + content['url']

    path.parent.mkdir(exist_ok=True)
    path.write_text(render(content['template'], attrs))
