# -*- coding: utf-8 -*-
import os

class FileWriter(object):
    """Class for writing site files."""

    def get_canonical_filename(self, name):
        """Get file name from given path or file.

        If name is not recognized as a file name a /index.html is added.
        Leading slashes are stripped off.
        """

        if not name.startswith('/'):
            name = '/%s' % name

        if not os.path.splitext(name)[1]:
            name = os.path.join(name, 'index.html')

        return name.lstrip('/')

    def getfile(self, dir_dst, path):
        """Determine file to create and return an open file handle for writing.

        Paths pointing to a file name will be created as they are. When a path points
        to a directory a file named index.html will be created in that directory.
        """

        filename = self.get_canonical_filename(path)

        # create target directory if it doesn't exist
        dir_target = os.path.join(dir_dst, os.path.dirname(filename))
        if not os.path.exists(dir_target):
            os.makedirs(dir_target)

        return open(os.path.join(dir_dst, filename), 'w')

    def write(self, file, content):
        """Write content to file and close it."""

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

        for field, val in doc.items():
            if isinstance(val, str):
                val = val.decode('utf-8')
            self.template.add_var(field, val)

    def write(self, doc, template):
        """Render and write document to created file.

        Returns False if template is False.
        """

        if not template:
            return False

        self.set_template_vars(doc)
        page = self.template.get_env().get_template(template)

        out = self.getfile(self.dir_dst, doc['url'])
        out.write(page.render(self.template.get_vars()).encode('utf-8'))
        out.close()