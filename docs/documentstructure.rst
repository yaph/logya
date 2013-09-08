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

Tags
^^^^

You can tag documents using the ``tags`` attribute, which is assigned a
list of comma separated tags, for example:

::

    tags: [example tag 1, example tag 2, example tag 3]

If you specify document tags the ``tags`` sub-directory will be created
containing indexes with links to the corresponding documents, in this
case don't create document URLs that start with ``/tags/``.

To create a list of links to these index pages from a post you can
access the ``tags_links`` template variable, which is populated
automatically and mustn't be specified manually in the document header:

::

    {% if tag_links %}
      {% for url, anchor in tag_links %}
        <span class="tag"><a href="{{url|e}}">{{anchor|e}}</a></span>
      {% endfor %}
    {% endif %}

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

    <h1>This is a heading</h1><p>This is a paragraph</p>

Markdown
^^^^^^^^

::

    # This is a heading

    This is a paragraph