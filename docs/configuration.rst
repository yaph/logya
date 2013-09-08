.. configuration:

Configuration
=============

Below you find configuration sections and settings:

[site] section
~~~~~~~~~~~~~~

All settings in this section will be available to all templates, so
names for configuration variables mustn't be used as names in document
headers.

**base\_url**
    ``base_url`` is the only required setting needed to create the
    canonical variable and to generate RSS feeds.

[templates] section
~~~~~~~~~~~~~~~~~~~

index
    The template to use for generated index.html files. If not set,
    indexes won't be created.
doc
    The template to use for generated content documents. If not set, the
    document won't be created.

[extensions] section
~~~~~~~~~~~~~~~~~~~~

Currently this section is not supported. I consider using it for turning
extensions on and off.