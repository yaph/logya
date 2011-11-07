# -*- coding: utf-8 -*-
import os

class FileWriter(object):
    """Class for writing site files."""

    def getfile(self, dir_dst, path):
        """Determine file name to create and return an open file handle for writing.

        Paths pointing to a file name will be created as they are. When a path points
        to a directory a file named index.html will be created in that directory.
        """

        directory = os.path.join(dir_dst, os.path.dirname(path).lstrip('/'))
        if not os.path.exists(directory):
            os.makedirs(directory)

        # the resulting filename won't have an extension for paths like /path/file
        filename = os.path.basename(path)
        if not filename:
            filename = 'index.html'
        return open(os.path.join(directory, filename), 'w')

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

    def write(self, doc):
        """Render and write document to created file."""

        self.set_template_vars(doc)
        page = self.template.get_env().get_template(doc['template'])
        f = self.getfile(self.dir_dst, doc['url'])
        f.write(page.render(self.template.get_vars()).encode('utf-8'))
        f.close()