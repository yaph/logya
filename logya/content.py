# -*- coding: utf-8 -*-
from datetime import datetime
from os import walk
from pathlib import Path

from markdown import markdown

from logya import allowed_exts
from logya.util import slugify

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def add_collections(doc, site_index, collections):
    for attr, values in doc.copy().items():
        if attr not in collections:
            continue
        root = collections[attr]['path']
        for value in values:
            collection_url = f'/{root}/{slugify(value.lower())}/'
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


def write_page(content, template, settings):
    page = ''

    # Make all settings in site section available to templates.
    template_vars = settings['site']

    # Make doc attributes available to templates.
    template_vars.update(content['doc'])

    # Set additional template variables.
    template_vars['canonical'] = settings['site']['base_url'] + template_vars['url']
    template_vars['collections'] = []
    template_vars['index'] = {}

    body = template_vars.get('body')
    if body:
        if content_type(content['path']) == 'markdown':
            template_vars['body'] = markdown(body, extensions=[
                'markdown.extensions.attr_list',
                'markdown.extensions.def_list',
                'markdown.extensions.fenced_code'])

        # Pre-render doc body so Jinja2 template tags can be used in content body.
        template_vars['body'] = template.env.from_string(body).render(template_vars)

    if 'template' in template_vars:
        page = template.env.get_template(template_vars['template']).render(template_vars)
    elif body:
        page = body

    Path(settings['paths']['public'], template_vars['url'], 'index.html').write_text(page)


def write_collection(path, content, template, settings):
    """Write an auto-generated index.html file."""

    template.vars['docs'] = content['docs']
    template.vars['title'] = content['title']
    template.vars['canonical'] = settings['site']['base_url'] + content['url']

    page = template.env.get_template(content['template'])
    path.parent.mkdir(exist_ok=True)
    path.write_text(page.render(template.vars))
