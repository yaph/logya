.. documentstructure:

Document Structure
==================

Documents are dived into header and body parts.

Document Header
~~~~~~~~~~~~~~~

The header is in `YAML <http://yaml.org/>`_ format. It starts and ends
with 3 dashes. In the header you must specify ``url`` and ``title``
other attributes such as description, scripts and style sheets are
optional. All attributes can be accessed in templates.

Attribute values can range from simple strings to nested data structures
that are automatically available in templates.

The only exception with a pre-defined value format is the ``created``
attribute. If you set it, it must adhere to the format
``YYYY-MM-DDTHH:MM:SS`` without surrounding quotes as shown in the
example. If you don't set the creation time in a document header, the
file modification time will be used for sorting documents in indexes.

::

    ---
    url: /
    title: Logya Documentation
    template: post.html
    created: 2012-03-18 13:59:16
    previewimage: /path/to/previewimage.png
    ---

Reserved Variable Names
^^^^^^^^^^^^^^^^^^^^^^^

Besides the mandatory content variables ``url`` and ``title`` and the ``base_url``
configuration variable, you mustn't use ``canonical`` and ``debug`` otherwise
their values will be overwritten. ``canonical`` with the canonical URL of the
current page including the host and ``debug`` will be set to ``True`` in serve
mode in other modes it is not set.

An example where the ``debug`` variable is useful: you want to use uncompressed
JavaScript files during development and use compressed ones on the live site.
You can do so using the following check in your template:

::

    {% if debug %}
        <script src="/js/script.js"></script>
    {% else %}
        <script src="/js/script.min.js"></script>
    {% endif %}

Indexes
^^^^^^^

You can create an index from one or more header attributes by adding a setting
for it in the site config and specifying a list of values in the doc header.
For example add an attribute called ``tags`` and assign it a list of comma
separated values:

::

    tags: [example tag 1, example tag 2, example tag 3]

If you specify document tags the ``tags`` sub-directory will be created
containing indexes with links to the corresponding documents, in this
case don't create document URLs that start with ``/tags/``.

To create a list of links to these index pages from a post you can
access the ``tags_links`` template variable, which is populated
automatically and mustn't be specified manually in the document header:

::

    {% if tags_links %}
      {% for url, anchor in tags_links %}
        <span class="tag"><a href="{{url|e}}">{{anchor|e}}</a></span>
      {% endfor %}
    {% endif %}

Alternatively you can use the provided links macro as follows:

::

    {% import 'macros/links.html' as links %}
    <p>Tags: {{ links.index(tags_links) }}</p>

Since this template variable is generated from the corresponding attribute name,
only use letters and underscores in it. Indexes can be created for header
attributes that contain a list of string values.

Document Body
~~~~~~~~~~~~~

The remaining part of the document is treated as the content that goes
in the body of the created HTML page. This content can either be written
in `markdown <http://daringfireball.net/projects/markdown/>`_ or marked
up with any HTML tag that can be in the body of an HTML document. The
body format is indicated by the file name extension.

HTML
^^^^

::

    <h1>This is a heading</h1>
    <p>This is a paragraph</p>

Markdown
^^^^^^^^

::

    # This is a heading

    This is a paragraph