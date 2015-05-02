.. directorylayout:

Directory Layout
================

The following folders and files are recognized when generating a Web
site with Logya.

content - required
~~~~~~~~~~~~~~~~~~

The content directory contains all of the site's documents. Documents
can be located in sub directories and must end in the file extensions
``.html``, ``.md`` or ``.markdown``.

templates - required
~~~~~~~~~~~~~~~~~~~~

The templates directory contains all of the site's Jinja2 templates.

site.yaml - required
~~~~~~~~~~~~~~~~~~~~

This file contains the site configuration in YAML format.

static - optional
~~~~~~~~~~~~~~~~~

This static directory contains all static resources like JavaScript,
CSS, image, and server configuration files.

bin - optional
~~~~~~~~~~~~~~

This directory contains scripts that are called during generation and
serving. Scripts can for example generate pages from content that is
fetched from a database or from the web.

Python scripts can access the logya object via the logya global
variable.