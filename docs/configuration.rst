.. configuration:

Configuration
=============

Below you find an example configuration and information about the different sections and settings.


Default configuration
~~~~~~~~~~~~~~~~~~~~~

::

    # General settings that will be available in templates.
    site:
        base_url: http://localhost:8080
        disqus_shortname: null
        author: Author


    # Settings that affect collections in the document index. Top-level keys of
    # collections can be used as document attributes for grouping it in the
    # corresponding collecion.
    collections:
        tags:
            path: tags
            template: index.html


    # Content specific settings, at the moment only templates are specified.
    content:
        index:
            template: index.html # default template used for collections
        doc:
            template: page.html
        rss:
            template: rss2.xml


    # Template specific settings.
    template:
        trim_whitespace: true

site section
~~~~~~~~~~~~

All settings in this section will be available to all templates, so names for configuration variables mustn't be used as names in document headers.

**base\_url**
    ``base_url`` is the only required setting needed to create the canonical variable and to generate RSS feeds.


collections section
~~~~~~~~~~~~~~~~~~~

This section allows to set document collections from header variables. The default configuration sets a collection for tags.


content section
~~~~~~~~~~~~~~~

This section is for setting the document, index and rss templates to use when generating the site.


template section
~~~~~~~~~~~~~~~~

This optional section is for template related settings. At the moment you can set whether to `trim whitespace <http://jinja.pocoo.org/docs/dev/templates/#whitespace-control>`_ around template tags.