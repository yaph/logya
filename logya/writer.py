# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from logya import path

from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


def encode_content(headers, body):
    """Encode headers and body in content format."""

    return '---\n{}\n---\n{}'.format(dump(headers, Dumper=Dumper).strip(), body)


def write(filename, content, create_dirs=True):
    """Write content to file.

    If create_dirs is true the parent directories of the file are created, if
    they do not exist yet.
    """

    if create_dirs:
        # create target directory if it doesn't exist
        target = os.path.dirname(filename)
        if not os.path.exists(target):
            os.makedirs(target)

    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def write_content(dir_target, headers, body):
    """Write a file that can be parsed as content.

    This is can be used in scripts that extend Logya, but is not used in core
    at the moment.
    """

    write(
        path.target_file(dir_target, headers['url']),
        encode_content(headers, body))


class DocWriter():
    """Class for writing site documents."""

    def __init__(self, dir_target, template):
        """Set required properties."""

        self.dir_target = dir_target
        self.template = template

    def write(self, doc, template):
        """Render and write document to created file."""

        # Make a copy so no previous doc attributes are retained, that don't
        # exist in current doc.
        tpl_vars = self.template.vars.copy()
        tpl_vars.update(doc)

        # Set additional template variables.
        tpl_vars['canonical'] = tpl_vars['base_url'] + tpl_vars['url']

        # Pre-render doc body so Jinja2 template tags can be used in content.
        body = ''
        if tpl_vars.get('body'):
            body = self.template.env.from_string(tpl_vars['body']).render(tpl_vars)
        tpl_vars['body'] = body

        page = self.template.env.get_template(template)
        content = page.render(tpl_vars)

        write(path.target_file(self.dir_target, doc['url']), content)
