.. templates:

Templates
=========

The template engine that comes with Logya is `jinja2 <http://jinja.pocoo.org/>`_. In addition to the many functions and filters jinja2 provides you can use the following filters and global functions.

attr_contains
-------------

The ``attr_contains`` filter returns a list of documents that have the given attribute and its value contains the given test value. Consider the following `real world usage example <http://guitarstreams.com/chord/guitar/C/>`_:

::

    {% set lessons = index['lesson/guitar'].docs|attr_contains('chords', 'C') %}

This template snippet selects the documents in the ``lesson/guitar`` index that have an attribute called ``chords`` containing the value ``C``. In this case the document attribute value is a list, but you can also check whether the value is ``in`` other Python sequence types, such as strings.

collection_index
----------------

The ``collection_index`` function returns a dictionary of collection tuple lists keyed by ASCII letters.

doc_index
---------

The ``doc_index`` function returns a dictionary of document object lists keyed by ASCII letters and sorted by an optionally specified attribute, which is set to ``title`` by default. An example of this function in use can be seen on `guitarstreams.com/musicians/ <https://guitarstreams.com/musicians/>`_.

filesource
----------

You can use the ``filesource`` function to include the text of an external file on a page. The optional ``limit`` parameter specifies how many lines to include, if not provided the whole file will be included. The file content is escaped by default, so that you can display HTML or other source code. The example below is taken from the `d3.geomap documentation <http://d3-geomap.github.io/>`_.

::

    {{ filesource('static/html/d3.geomap.html') }}
    {{ filesource('static/js/maps/world-plain.js') }}

The file to include must be passed as a name relative to the site's root directory or as an absolute file name. The latter is discouraged though, because it'll cause trouble when you move your site directory.

This function is mainly intended for documentation purposes as it allows you to include the same source code that is used to render an example visible on the current page. Restricting the number of lines works as follows.

::

    <pre>{{ filesource(data, lines=6) }}</pre>

To not escape the content, you can set raw to True.

::

    <pre>{{ filesource(data, raw=True) }}</pre>

This can be used for example to inline SVG code when using SVG sprites.

slugiy
------

Use this filter to change a string so it can be used as part of a URL.

::

    <pre>{{ string|slug }}</pre>

get_doc
-------

You can use the ``get_doc`` function to get a document object via its URL, which allows you to create links between documents. Say document A has a ``link`` property set to the URL of document B. You can then get an object representing B and link to it from within A's template like so:

::

    {% set B = get_doc(link) %}
    <a href="{{ B.url }}">{{ B.title }}</a>
