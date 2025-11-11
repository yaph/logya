import sys
from datetime import datetime
from functools import lru_cache
from operator import itemgetter
from pathlib import Path
from string import ascii_lowercase
from typing import Any

from jinja2 import Environment, FileSystemBytecodeCache, FileSystemLoader, exceptions
from markupsafe import escape

from logya.util import slugify

env = Environment(
    autoescape=False,  # noqa: S701 # Disable autoescaping to allow raw HTML in templates.
    lstrip_blocks=True,
    trim_blocks=True,
)


def _alpha_index(
    items: list, non_ascii_key: str = '_', sort_attr: str = 'title', sort_order: str = 'ascending'
) -> dict:
    """Return an alphabetical index for a list of dicts. All strings that do not start with an ASCII letter are stored
    in `non_ascii_key`.
    """

    index: dict[str, list] = {}

    for item in items:
        value = item[sort_attr]
        key = value.lower()[0]
        if key not in ascii_lowercase:
            key = non_ascii_key
        index[key] = [*index.get(key, []), item]

    reverse = sort_order != 'ascending'
    keys = sorted(index.keys(), reverse=reverse)
    return {key: sorted(index[key], key=itemgetter(sort_attr)) for key in keys}


def _filesource(root: Path, name: str, lines: int | None = None, raw: bool = False) -> str | None:
    """Read and return source of text files.

    A template function that reads the source of the given file and returns it. Content is escaped by default so it can
    be rendered safely on a Web page. The lines keyword argument is used to limit the number of lines returned. To not
    escape the content you can set the raw keyword argument to False. A use case is for documentation projects to show
    the source code used to render the current example.
    """

    # Call lstrip to prevent loading files outside the site directory.
    path_src = root.joinpath(name.lstrip('/'))
    try:
        text = path_src.read_text()
    except UnicodeDecodeError:
        print(f'Error reading: {path_src.as_posix()}')
        return None
    if lines:
        text = '\n'.join(text.split('\n')[:lines])
    if raw:
        return text
    return escape(text)


def _sort_docs(item: dict, key: str) -> Any:
    """Return sort value from item and use casefold for strings to make sorting case insensitive."""
    value = item.get(key)
    return value.casefold() if isinstance(value, str) else value


@lru_cache(maxsize=256)
def _get_docs(L, url: str, sort_attr: str = 'created', sort_order: str = 'descending') -> list:
    docs = []
    # A collection index will only exist at the given URL if there is no content document with the same URL.
    if coll := L.collection_index.get(url):
        docs = coll['docs']
    if not docs:
        for doc_url, content in L.doc_index.items():
            if doc_url.startswith(url):
                docs.append(content['doc'])

    reverse = sort_order == 'descending'
    return sorted((d for d in docs if sort_attr in d), key=lambda item: _sort_docs(item, sort_attr), reverse=reverse)


def add_filters() -> None:
    # Create an alphabetical index for a list of objects.
    env.filters['alpha_index'] = _alpha_index
    # Filter docs list where the given attribute contains the given value.
    env.filters['attr_contains'] = lambda docs, attr, val: [d for d in docs if val in d.get(attr, '')]
    # Make slugify available
    env.filters['slugify'] = slugify


def add_globals(L) -> None:
    # Include the source of a file.
    env.globals['filesource'] = lambda name, **kwargs: _filesource(L.paths.root, name, **kwargs)
    # Get collection from its name.
    env.globals['get_collection'] = lambda name: L.collections.get(name)
    # Get a document from its URL.
    env.globals['get_doc'] = lambda url: L.doc_index.get(url)['doc']
    # Get documents from a URL.
    env.globals['get_docs'] = lambda url='', **kwargs: _get_docs(L, url, **kwargs)
    # Make current datetime available.
    env.globals['now'] = datetime.now
    # Include the site settings last.
    env.globals.update(L.settings['site'])


def init_env(L):
    if not L.paths.templates.exists() or not L.paths.templates.is_dir():
        sys.exit('No templates directory found.')

    env.loader = FileSystemLoader(L.paths.templates)

    for ext in L.jinja_extensions:
        env.add_extension(ext)

    # Try to setup Bytecode cache for templates.
    try:
        L.paths.cache.mkdir(parents=True, exist_ok=True)
        env.bytecode_cache = FileSystemBytecodeCache(L.paths.cache.as_posix())
    except OSError:
        env.bytecode_cache = None

    add_filters()
    add_globals(L)


def render(variables: dict) -> str:
    # Pre-render enables the use of Jinja2 template syntax in attribute values.
    for attr in variables.get('pre_render', []):
        variables[attr] = env.from_string(variables[attr]).render(variables)

    try:
        return env.get_template(variables['template']).render(variables)
    except (TypeError, exceptions.UndefinedError) as err:
        sys.exit(f'Error rendering: {variables}\n{err}\nExiting...')
