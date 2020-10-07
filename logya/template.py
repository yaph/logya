# -*- coding: utf-8 -*-
from operator import itemgetter

from jinja2 import Environment, FileSystemLoader

from logya.util import deduplicate


env = Environment(
    loader=FileSystemLoader('templates'),
    lstrip_blocks=True,
    trim_blocks=True
)


def _content_list(index: dict, url: str = '') -> list:
    content = index.get(url)
    if content:
        return content.get('docs', [content.get('doc')])
    return []


def _collection_index(
        docs: list,
        non_ascii_key='_',
        sort_attr: str = 'created',
        sort_order: str = 'descending') -> dict:
    """Return an alphabetical index for a collection, i. e. a list of (URL, name) tuples.
    All strings that do not start with an ASCII letter are stored in `non_ascii_key`.
    """
    pass
    # collection_index = {}
    # for t in collection:
    #     key = t[1].lower()[0]
    #     if key not in ascii_lowercase:
    #         key = non_ascii_key
    #     collection_index[key] = index.get(key, []) + [t]
    # return {key: sorted(collection_index[key]) for key in sorted(collection_index.keys())}


def _get_docs(index: dict, url: str = '', sort_attr: str = 'created', sort_order: str = 'descending') -> list:
    docs = []
    if url:
        docs = _content_list(index, url)
    if not docs:
        for doc_url, content in index.items():
            if doc_url.startswith(url):
                docs.extend(_content_list(index, doc_url))

    reverse = True if sort_order == 'descending' else False
    return sorted(deduplicate(docs, attr='url'), key=itemgetter(sort_attr), reverse=reverse)


def init_env(settings, site_index):
    # Enable break and continue in templates.
    env.add_extension('jinja2.ext.loopcontrols')
    # Enable with statement for nested variable scopes.
    env.add_extension('jinja2.ext.with_')
    # Enable expression-statement extension that adds the do tag.
    env.add_extension('jinja2.ext.do')

    # Get a document from its URL.
    env.globals['get_doc'] = lambda url: site_index.get(url)['doc']

    # Get documents from a URL.
    env.globals['get_docs'] = lambda **kwargs: _get_docs(site_index, **kwargs)

    # Return an alphabetical index for a collection.
    env.globals['collection_index'] = lambda **kwargs: _collection_index(site_index, **kwargs)

    # Filter docs list where the given attribute contains the given value.
    env.filters['attr_contains'] = lambda docs, attr, val: [
        doc for doc in docs if attr in doc and val in doc[attr]]


def render(tpl, variables, pre_render=None):
    # Pre-render enables the use of Jinja2 template tags in the value of the given attribute.
    if pre_render and pre_render in variables:
        variables[pre_render] = env.from_string(variables[pre_render]).render(variables)
    return env.get_template(tpl).render(variables)
