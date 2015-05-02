# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from logya import allowed_exts


class FileWriter(object):
    """Class for writing site files."""

    def canonical_filename(self, name):
        """Get file name from given path or file.

        If name is not recognized as a file name a /index.html is added. To be
        recognized as a file name it must end with an allowed extension.
        Leading slashes are stripped off.
        """

        # TODO explain this
        if not name.startswith('/'):
            name = '/{}'.format(name)

        # only allowed extension will be written to a file, otherwise a
        # directory with the name is created and content written to index.html
        ext = os.path.splitext(name)[1]
        if not ext or ext.lstrip('.') not in allowed_exts:
            name = os.path.join(name, 'index.html')

        return name.lstrip('/')

    def file_handle(self, dir_dst, path):
        """Determine file to create and return an open file handle for writing.

        Paths pointing to a file name will be created as they are. When a path
        points to a directory a file named index.html will be created in that
        directory.
        """

        filename = self.canonical_filename(path)
        # create target directory if it doesn't exist
        dir_target = os.path.join(dir_dst, os.path.dirname(filename))
        if not os.path.exists(dir_target):
            os.makedirs(dir_target)
        return io.open(os.path.join(dir_dst, filename), 'w', encoding='utf-8')

    def write(self, fh, content):
        """Write content to file and close it."""

        fh.write(content)
        fh.close()


class DocWriter(FileWriter):
    """Class for writing site documents."""

    def __init__(self, dir_dst, template):
        """Set required properties."""

        self.dir_dst = dir_dst
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
            print('Warning: doc {} has no template set and won\'t be created.'
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
        out = self.file_handle(self.dir_dst, doc['url'])

        content = page.render(tpl_vars)

        out.write(content)
        out.close()
