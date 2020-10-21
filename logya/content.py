# -*- coding: utf-8 -*-
from datetime import datetime
from operator import itemgetter
from pathlib import Path

from markdown import markdown

from logya.template import render
from logya.util import load_yaml, slugify


# Extensions of content files that will be processed.
process_extensions = {
    '.css',
    '.htm',
    '.html',
    '.js',
    '.json',
    '.markdown',
    '.md',
    '.php',
    '.txt',
    '.xml'
}

# Extensions of content files that will be removed.
remove_extensions = {
    '.htm',
    '.html',
    '.markdown',
    '.md'
}


def content_type(path: Path) -> str:
    """Return content type based in file extensions."""

    if path.suffix in {'.html', '.htm'}:
        return 'html'
    if path.suffix in {'.md', '.markdown'}:
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


def filepath(base: Path, url: str) -> Path:
    """Get a Path object pointing to a file.

    If url does not end in a file name 'index.html' will be appended.
    """

    path = Path(base, url.lstrip('/'))
    if not path.suffix or path.suffix not in process_extensions:
        path = path.joinpath('index.html')
    return path


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


def read(path: Path, path_rel: Path) -> str:
    content = path.read_text().strip()
    try:
        doc = parse(content, content_type=content_type(path))
    except Exception as err:
        print(f'Error parsing: {path}\n{err}')
        return

    # Ensure doc has a title.
    doc['title'] = doc.get('title', path.stem)

    # URLs set in the document are prioritized and left unchanged.
    doc['url'] = doc.get('url', create_url(path_rel))

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


def write_doc(path: Path, content: dict, settings: dict):
    """Write a document page."""

    path.parent.mkdir(parents=True, exist_ok=True)
    attrs = content['doc'].copy()
    if 'body' in attrs and content_type(content['path']) == 'markdown':
        attrs['body'] = markdown(attrs['body'], extensions=settings.get('extensions', {}).get('markdown', []))
    path.write_text(render(attrs, pre_render='body'))


def write_collection(path: Path, content: dict):
    """Write a collection page.

    Documents are sorted by created datetime in descending order.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    content['docs'].sort(key=itemgetter('created'), reverse=True)
    path.write_text(render(content))
