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


def content_type(path: Path) -> str | None:
    """Return content type based in file extensions."""

    if path.suffix in {'.html', '.htm'}:
        return 'html'
    if path.suffix in {'.md', '.markdown'}:
        return 'markdown'
    return None


def create_url(path: Path) -> str:
    """Return document URL based on source file path."""

    suffix = ''
    if path.suffix in remove_extensions:
        suffix = '/'
        path = Path(path.parent) if path.stem == 'index' else path.parent.joinpath(path.stem)

    if not path.parts:
        return '/'

    return f'/{"/".join(slugify(p) for p in path.parts)}{suffix}'


def filepath(base: Path, url: str) -> Path:
    """Get a Path object pointing to a file.

    If url does not end in a file name 'index.html' will be appended.
    """

    path = base.joinpath(url.lstrip('/'))
    if not path.suffix or path.suffix not in process_extensions:
        path = path.joinpath('index.html')
    return path


def parse(content: str) -> dict:
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


def read(path: Path, path_rel: Path, markdown_extensions: list) -> dict | None:
    try:
        doc = parse(path.read_text().strip())
    except Exception as err:
        print(f'Error reading/parsing: {path}\n{err}')
        return None

    if content_type(path) == 'markdown':
        doc['body'] = markdown(doc['body'], extensions=markdown_extensions)

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


def write_page(base_path: Path, content: dict) -> None:
    """Write a rendered content page."""

    path_page = filepath(base_path, content['url'])
    path_page.parent.mkdir(parents=True, exist_ok=True)
    path_page.write_text(render(content))


def write_collection(base_path: Path, content: dict) -> None:
    """Write a collection page.

    Documents are sorted by created datetime in descending order.
    """

    content['docs'].sort(key=itemgetter('created'), reverse=True)
    write_page(base_path, content)
