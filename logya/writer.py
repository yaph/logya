# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from logya import path


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


class DocWriter():
    """Class for writing site documents."""

    def __init__(self, dir_target, template):
        """Set required properties."""

        self.dir_target = dir_target
        self.template = template

    def set_template_vars(self, doc):
        """Set template variables."""

        # empty doc vars dictionary to not retain previous doc values
        self.template.doc_vars = {}
        for field, val in list(doc.items()):
            self.template.doc_vars[field] = val

    def write(self, doc, template):
        """Render and write document to created file.

        Returns False if template is False.
        """

        if not template:
            print('Warning: {} has no template set and won\'t be created.'
                  .format(doc['url']))
            return False

        self.set_template_vars(doc)
        tpl_vars = self.template.all_vars

        # Set additional template variables.
        tpl_vars['canonical'] = tpl_vars['base_url'] + tpl_vars['url']

        # Pre-render doc body so Jinja2 template tags can be used in content.
        tpl_vars['body'] = self.template.env.from_string(
            tpl_vars.get('body', '')).render(tpl_vars)

        page = self.template.env.get_template(template)
        content = page.render(tpl_vars)

        write(path.target_file(self.dir_target, doc['url']), content)
