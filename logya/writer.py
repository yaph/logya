# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os

from logya import path


def target_file(basedir, url, create_dirs=True):
    filename = path.canonical_filename(url)

    if create_dirs:
        # create target directory if it doesn't exist
        target = os.path.join(basedir, os.path.dirname(filename))
        if not os.path.exists(target):
            os.makedirs(target)

    return os.path.join(basedir, filename)


class FileWriter(object):
    """Class for writing site files."""

    def file_handle(self, dir_dst, url):
        """Determine file to create and return an open file handle for writing.

        URLs pointing to a file name will be created as they are. When a url
        points to a directory a file named index.html will be created in that
        directory.
        """

        filename = path.canonical_filename(url)
        # create target directory if it doesn't exist
        dir_target = os.path.join(dir_dst, os.path.dirname(filename))
        if not os.path.exists(dir_target):
            os.makedirs(dir_target)

        tpl = 'dir_dst: {}\nurl: {}\nfilename: {}\ntarget: {}\nfile: {}\n\n'
        print(tpl.format(
            dir_dst, url, filename, dir_target, os.path.join(dir_dst, filename)))

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
