# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(),
    lstrip_blocks=True,
    trim_blocks=True
)


def init(settings, site_index):
    # Enable break and continue in templates.
    env.add_extension('jinja2.ext.loopcontrols')
    # Enable with statement for nested variable scopes.
    env.add_extension('jinja2.ext.with_')
    # Enable expression-statement extension that adds the do tag.
    env.add_extension('jinja2.ext.do')

    # Get a document from its URL.
    env.globals['get_doc'] = lambda url: site_index.get(url)['doc']

    # Filter docs list where the given attribute contains the given value.
    env.filters['attr_contains'] = lambda docs, attr, val: [
        doc for doc in docs if attr in doc and val in doc[attr]]


def render(tpl, variables, pre_render=None):
    # Pre-render enables the use of Jinja2 template tags in the value of the given attribute.
    if pre_render and pre_render in variables:
        variables[pre_render] = env.from_string(variables[pre_render]).render(variables)
    return env.get_template(tpl).render(variables)










