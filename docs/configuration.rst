.. _configuration:

Configuration
=============

Below you find an explanation of the sections and settings in the ``site.yaml`` configuration file.

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


languages section
~~~~~~~~~~~~~~~~~

The languages section is optional and exists to enable additional features for multilingual sites. Please see :ref:`I18N <i18n>` for more information.