.. directorylayout:

Directory Layout
================

The following folders and files are recognized when generating a Web site with Logya.

content - required
~~~~~~~~~~~~~~~~~~

The content directory contains all of the site's documents. Documents can be located in arbitrary sub directories. To be loaded and parsed as content a file must end in one of the following extensions: ``html``, ``htm``, ``xml``, ``json``, ``js``, ``css``, ``php``, ``md``, ``markdown``, ``txt``.

templates - required
~~~~~~~~~~~~~~~~~~~~

The templates directory contains all of the site's Jinja2 templates.

site.yaml - required
~~~~~~~~~~~~~~~~~~~~

This file contains the site configuration in YAML format.

static - optional
~~~~~~~~~~~~~~~~~

This static directory contains all static resources like JavaScript, CSS, image, and server configuration files.
