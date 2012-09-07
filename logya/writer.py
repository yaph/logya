# -*- coding: utf-8 -*-
import os


class FileWriter(object):
    """Class for writing site files."""

    allowed_exts = ['html', 'htm', 'xml', 'json', 'js', 'css', 'php', 'md', 'markdown']

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
        if not fext or fext.lstrip('.') not in self.allowed_exts:
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

        # empty doc vars dictionary to not retain previous doc values
        self.template.empty_doc_vars()
        for field, val in doc.items():
            if isinstance(val, str):
                val = val.decode('utf-8')
            self.template.add_doc_var(field, val)


    def write(self, doc, template):
        """Render and write document to created file.

        Returns False if template is False.
        """

        if not template: return False

        self.set_template_vars(doc)
        tpl_vars = self.template.get_all_vars()
        tpl_vars['canonical'] = tpl_vars['base_url'] + tpl_vars['url']

        page = self.template.get_env().get_template(template)
        out = self.getfile(self.dir_dst, doc['url'])
        out.write(page.render(tpl_vars).encode('utf-8'))
        out.close()

