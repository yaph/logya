# -*- coding: utf-8 -*-
import os

from logya.compat import file_open as open
from logya.compat import is3
from logya.globals import allowed_exts


class FileWriter(object):
    """Class for writing site files."""

    def get_canonical_filename(self, name):
        """Get file name from given path or file.

        If name is not recognized as a file name a /index.html is added.
        To be recognized as a file name it must end in one of self.allowed_exts.
        Leading slashes are stripped off.
        """

        # TODO explain this
        if not name.startswith('/'):
            name = '/%s' % name

        # only allowed extension will be written to a file, otherwise a
        # directory with the name is created and content written to index.html
        fext = os.path.splitext(name)[1]
        if not fext or fext.lstrip('.') not in allowed_exts:
            name = os.path.join(name, 'index.html')

        return name.lstrip('/')

    def getfile(self, dir_dst, path):
        """Determine file to create and return an open file handle for writing.

        Paths pointing to a file name will be created as they are. When a path
        points to a directory a file named index.html will be created in that
        directory.
        """

        filename = self.get_canonical_filename(path)
        # create target directory if it doesn't exist
        dir_target = os.path.join(dir_dst, os.path.dirname(filename))
        if not os.path.exists(dir_target):
            os.makedirs(dir_target)
        return open(os.path.join(dir_dst, filename), 'w', encoding='utf-8')

    def write(self, file, content):
        """Write content to file and close it."""

        if not is3:
            content = content.encode('utf-8')
        file.write(content)
        file.close()


class DocWriter(FileWriter):
    """Class for writing site documents."""

    def __init__(self, dir_dst, template):
        """Set required properties."""

        self.dir_dst = dir_dst
        self.template = template

    def set_template_vars(self, doc):
        """Set template variables."""

        # empty doc vars dictionary to not retain previous doc values
        self.template.empty_doc_vars()
        for field, val in list(doc.items()):
            if isinstance(val, str) and not is3:
                val = val.decode('utf-8')
            self.template.add_doc_var(field, val)

    def write(self, doc, template):
        """Render and write document to created file.

        Returns False if template is False.
        """

        if not template:
            print(('Warning: doc %s has no template set and won\'t be created.'
                % doc['url']))
            return False

        self.set_template_vars(doc)
        tpl_vars = self.template.get_all_vars()
        tpl_vars['canonical'] = tpl_vars['base_url'] + tpl_vars['url']

        page = self.template.get_env().get_template(template)
        out = self.getfile(self.dir_dst, doc['url'])

        content = page.render(tpl_vars)
        if not is3:
            content = content.encode('utf-8')

        out.write(content)
        out.close()