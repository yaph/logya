# -*- coding: utf-8 -*-
from operator import itemgetter
from pathlib import Path
from string import ascii_lowercase

from jinja2 import Environment, FileSystemLoader, escape


env = Environment(
    loader=FileSystemLoader('templates'),
    lstrip_blocks=True,
    trim_blocks=True
)


def _alpha_index(
        items: list,
        non_ascii_key: str = '_',
        sort_attr: str = 'title',
        sort_order: str = 'ascending') -> dict:
    """Return an alphabetical index for a list of dicts. All strings that do not start with an ASCII letter are stored
    in `non_ascii_key`.
    """

    index = {}

    for item in items:
        value = item[sort_attr]
        key = value.lower()[0]
        if key not in ascii_lowercase:
            key = non_ascii_key
        index[key] = index.get(key, []) + [item]

    reverse = False if sort_order == 'ascending' else True
    keys = sorted(index.keys(), reverse=reverse)
    return {key: sorted(index[key], key=itemgetter(sort_attr)) for key in keys}


def _filesource(root: Path, name: str, lines: int = None, raw: bool = False) -> str:
    """Read and return source of text files.

    A template function that reads the source of the given file and returns it. Content is escaped by default so it can
    be rendered safely on a Web page. The lines keyword argument is used to limit the number of lines returned. To not
    escape the content you can set the raw keyword argument to False. A use case is for documentation projects to show
    the source code used to render the current example.
    """

    # Call lstrip to prevent loading files outside the site directory.
    text = root.joinpath(name.lstrip('/')).read_text()
    if lines:
        text = '\n'.join(text.split('\n')[:lines])
    if raw:
        return text
    return escape(text)


def _get_docs(L, url: str, sort_attr: str = 'created', sort_order: str = 'descending') -> list:
    docs = []
    # A collection index will only exist at the given URL if there is no content document with the same URL.
    if coll := L.collection_index.get(url):
        docs = coll['docs']
    if not docs:
        for doc_url, content in L.doc_index.items():
            if doc_url.startswith(url):
                docs.append(content['doc'])

    reverse = True if sort_order == 'descending' else False
    return sorted((d for d in docs if sort_attr in d), key=itemgetter(sort_attr), reverse=reverse)


def init_env(L):
    # Enable break and continue in templates.
    env.add_extension('jinja2.ext.loopcontrols')
    # Enable with statement for nested variable scopes.
    env.add_extension('jinja2.ext.with_')
    # Enable expression-statement extension that adds the do tag.
    env.add_extension('jinja2.ext.do')

    # Create an alphabetical index for a list of objects.
    env.filters['alpha_index'] = _alpha_index

    # Include the source of a file.
    env.globals['filesource'] = lambda name, **kwargs: _filesource(L.paths.root, name, **kwargs)

    # Get a document from its URL.
    env.globals['get_doc'] = lambda url: L.doc_index.get(url)['doc']

    # Get documents from a URL.
    env.globals['get_docs'] = lambda url='', **kwargs: _get_docs(L, url, **kwargs)

    # Get collection from its name.
    env.globals['get_collection'] = lambda name: L.collections.get(name)

    # Filter docs list where the given attribute contains the given value.
    env.filters['attr_contains'] = lambda docs, attr, val: [
        doc for doc in docs if attr in doc and val in doc[attr]]


def render(tpl, variables, pre_render=None):
    # Pre-render enables the use of Jinja2 template tags in the value of the given attribute.
    if pre_render and pre_render in variables:
        variables[pre_render] = env.from_string(variables[pre_render]).render(variables)
    return env.get_template(tpl).render(variables)
