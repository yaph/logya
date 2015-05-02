.. configuration:

Configuration
=============

Below you find an example configuration and information about the different
sections and settings.


Default configuration
~~~~~~~~~~~~~~~~~~~~~

::

    site:
      base_url: http://localhost:8080
      disqus_shortname: null

    indexes:
    - path: tags
      var: tags

    templates:
    - content_type: index
      template: index.html
    - content_type: doc
      template: post.html


site section
~~~~~~~~~~~~

All settings in this section will be available to all templates, so
names for configuration variables mustn't be used as names in document
headers.

**base\_url**
    ``base_url`` is the only required setting needed to create the
    canonical variable and to generate RSS feeds.


indexes section
~~~~~~~~~~~~~~~

This section allows to set additional indexes from document header variables.
The default configuration sets an index for tags.


templates section
~~~~~~~~~~~~~~~~~

This section is for setting the default document and index templates.