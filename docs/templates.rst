.. templates:

Templates
=========

The template engine that comes with Logya is `jinja2 <http://jinja.pocoo.org/>`_. In addition to the many functions and filters jinja2 provides you can use the following filters/functions.

filesource
----------

You can use the ``filesource`` function to include the text of an external file on a page. The optional ``limit`` parameter specifies how many lines to include, if not provided the whole file will be included. The file content is escaped by default, so that you can display HTML or other source code. The example below is taken from the `d3.geomap documentation <http://d3-geomap.github.io/>`_.

::

    {{ filesource('static/html/d3.geomap.html') }}
    {{ filesource('static/js/maps/world-plain.js') }}

The file to include must be passed as a name relative to the site's root directory or as an absolute file name. The latter is discouraged though, because it'll cause trouble when you move your site directory.

This function is mainly intended for documentation purposes as it allows you to include the same source code that is used to render an example visible on the current page. Restricting the number of lines works as follows.

::

    <pre>{{ filesource(data, lines=6) }}...</pre>

To not escape the content, you can set raw to True.

::

    <pre>{{ filesource(data, raw=True) }}...</pre>

This can be used for example to inline SVG code when using SVG sprites.

get_doc
-------

You can use the ``get_doc`` function to get a document object via its URL, which allows you to create links between documents. Say document A has a ``link`` property set to the URL of document B. You can then get an object representing B and link to it from within A's template like so:

::

    {% set B = get_doc(link) %}
    <a href="{{ B.url }}">{{ B.title }}</a>
