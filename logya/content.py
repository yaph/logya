# -*- coding: utf-8 -*-
from datetime import datetime
from os import walk
from pathlib import Path

from markdown import markdown

from logya.template import render
from logya.util import load_yaml, slugify


markdown_extensions = [
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.fenced_code']

# Extensions of content files that will be processed.
process_extensions = {
    '.html',
    '.htm',
    '.xml',
    '.json',
    '.js',
    '.css',
    '.php',
    '.md',
    '.markdown',
    '.txt'
}

# Extensions of content files that will be removed.
remove_extensions = {
    '.htm',
    '.html',
    '.markdown',
    '.md'
}


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
                        break
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


def content_type(path: Path) -> str:
    """Return content type based in file extensions."""

    if path.suffix in ['.html', '.htm']:
        return 'html'
    if path.suffix in ['.md', '.markdown']:
        return 'markdown'


def create_url(path: Path) -> str:
    """Return document URL based on source file path."""

    suffix = ''
    if path.suffix in remove_extensions:
        suffix = '/'
        if 'index' == path.stem:
            path = Path(path.parent)
        else:
            path = path.parent.joinpath(path.stem)

    if not path.parts:
        return '/'

    return f'/{"/".join(slugify(p) for p in path.parts)}{suffix}'


def parse(content: str, content_type: str = None) -> dict:
    """Parse document and return a dictionary of header fields and body."""

    # Extract YAML header and body and load header into dict.
    lines = content.splitlines()

    header_start = lines.index('---') + 1
    header_end = lines[header_start:].index('---') + 1
    header = '\n'.join(lines[header_start:header_end])
    body = '\n'.join(lines[header_end + 1:]).strip()
    parsed = load_yaml(header)
    parsed['body'] = body
    return parsed


def read(path: Path, paths) -> str:
    content = path.read_text().strip()
    try:
        doc = parse(content, content_type=content_type(path))
    except Exception as err:
        print(f'Error parsing: {path}\n{err}')
        return

    # Ensure doc has a title.
    doc['title'] = doc.get('title', path.stem)

    # URLs set in the document are prioritized and left unchanged.
    doc['url'] = doc.get('url', create_url(path.relative_to(paths.content)))

    # Use file modification time for created and updated attributes if not set in document.
    modified = datetime.fromtimestamp(path.stat().st_mtime)
    for attr in ['created', 'updated']:
        doc[attr] = doc.get(attr, modified)
        if isinstance(doc[attr], str):
            try:
                doc[attr] = datetime.fromisoformat(doc[attr])
            except ValueError:
                print(f'"{attr}" could not be converted to datetime. URL: {doc["url"]}')

    return doc


def read_all(paths, settings):
    # Index mapping URLs to content objects
    index = {}
    collections = settings.get('collections')

    for root, _, files in walk(paths.content):
        for f in files:
            path = Path(root, f)
            if path not in process_extensions:
                continue
            doc = read(path, paths)
            if doc:
                if collections:
                    add_collections(doc, index, collections)
                index[doc['url']] = {'doc': doc, 'path': path}

    return index


def write_page(path, content, settings):
    path.parent.mkdir(parents=True, exist_ok=True)

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

    path.parent.mkdir(parents=True, exist_ok=True)

    attrs = settings['site']
    attrs['docs'] = content['docs']
    attrs['title'] = content['title']
    attrs['canonical'] = settings['site']['base_url'] + content['url']

    path.write_text(render(content['template'], attrs))
