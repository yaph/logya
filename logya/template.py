# -*- coding: utf-8 -*-
import io
import os

from jinja2 import Environment, BaseLoader, TemplateNotFound, escape


def filesource(logya_inst, name, lines=None, raw=False):
    """Read and return source of text files.

    A template function that reads the source of the given file and returns it.
    Content is escaped by default so it can be rendered safely on a Web page.

    The lines keyword argument is used to limit the number of lines returned.

    To not escape the content you can set the raw keyword argument to False.

    A use case is for documentation projects to show the source code used
    to render the current example.
    """

    fname = os.path.join(logya_inst.dir_site, name)
    with io.open(fname, 'r', encoding='utf-8') as f:
        if lines is None:
            content = f.read()
        else:
            content = ''.join(f.readlines()[:lines])
    if raw:
        return content

    return escape(content)


def get_doc(logya_inst, url):
    """Get document located at given URL."""

    return logya_inst.docs.get(url)


class Template():
    """Class to handle templates."""

    def __init__(self, logya_inst):
        """Initialize template environment."""

        self.vars = {}
        self.dir_templates = logya_inst.dir_templates
        self.env = Environment(loader=TemplateLoader(self.dir_templates))

        # Enable break and continue in templates.
        self.env.add_extension('jinja2.ext.loopcontrols')

        # Enable with statement for nested variable scopes.
        self.env.add_extension('jinja2.ext.with_')

        # Enable expression-statement extension that adds the do tag.
        self.env.add_extension('jinja2.ext.do')

        # Trim whitespace around template tags if configured.
        tpl_settings = logya_inst.config.get('template')
        if tpl_settings and tpl_settings.get('trim_whitespace'):
            self.env.lstrip_blocks = True
            self.env.trim_blocks = True

        # Include the source of a file.
        self.env.globals['filesource'] = lambda x, lines=None, raw=False: filesource(
            logya_inst, x, lines=lines, raw=raw)

        # Get a document from its URL.
        self.env.globals['get_doc'] = lambda x: get_doc(logya_inst, x)

        # Filter docs list where the given attribute contains the given value.
        self.env.filters['attr_contains'] = lambda docs, attr, val: [
            doc for doc in docs if attr in doc and val in doc[attr]]

    def get_page(self, doc, template):
        try:
            page = self.env.get_template(template)
        except TemplateNotFound as err:
            raise TemplateNotFound('Doc: {}\n{}'.format(doc, err))
        return page


class TemplateLoader(BaseLoader):

    """Class to handle template Loading."""

    def __init__(self, path):
        """Set template path."""

        self.path = path

    def get_source(self, environment, template):
        """Set template source."""

        path = os.path.join(self.path, template)
        if not os.path.exists(path):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        with io.open(path, 'r', encoding='utf-8') as f:
            source = f.read()
        return source, path, lambda: mtime == os.path.getmtime(path)
