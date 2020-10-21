---
page: 4
title: Document Structure
template: page.html
created: 2013-09-08 19:45:45
---
# Document Structure

Documents are dived into header and body parts.

## Document Header

    ---
    title: Logya Documentation
    template: page.html
    created: 2012-03-18 13:59:16
    image: /path/to/image.png
    ---

The header is in [YAML](http://yaml.org/) format. It starts and ends with 3 dashes. The header is used for setting document attributes, that can be of arbitrary complexity and are accessible in templates. You can set a meta description, the scripts and stylesheets to include and whatever is useful in your scenario. The following attributes are reserved to have special meanings.

### body

Don't set a `body` attribute in the document header. It will be set to the body of the document automatically. An existing value will be overwritten.

### template

This is the only required attribute. Set it to the Jinja2 template to use for rendering the document. The template file name has to be specified relative to the `templates` directory.

### title

Setting a document `title` is highly recommended, but if not present the stem part of the content file name will be set as the document title.

### url

You can manually set a `url` attribute, which must be unique and can be used to refer to a document in templates. If you omit the `url` it will be created from the file name, e. g. the document in `content/book/chapter-1.html` will get the URL `/book/chapter-1/` with the file extension removed. File extensions are removed from HTML and Markdown files.

### created

If you specify a `created` datetime, you must use the format `YYYY-MM-DD HH:MM:SS` as shown in the example. Otherwise it will be set to the file modification time. I recommend setting this manually to the date of first publication. When you call the `get_docs` function in templates, by default documents will be sorted by `created` in descending order, so newest documents show up first. This is also the order in which documents appear in automatically created collection pages.

### updated

The `updated` datetime works like `created` and should show when the document was last edited. This can be useful if you want to highlight an edit, but typically the default value is fine.

---

### Collections

You can create a document collection to be included in the index from
one or more header attributes by adding a setting for it in the site
config and specifying a list of values in the doc header.

For example add an attribute called `tags` and assign it a list of comma
separated values:

    tags: [example tag 1, example tag 2, example tag 3]

If you specify document tags the `tags` sub-directory will be added to
the document index, containing links to the corresponding documents. If
you do this, don\'t create document URLs that start with `/tags/`, the
same applies to other user-defined index headers.

To create a list of links to these index pages from a post you can
access the `tags_links` template variable, which is populated
automatically and mustn\'t be specified manually in the document header:

    {% if tags_links %}
      {% for url, anchor in tags_links %}
        <span class="tag"><a href="{{url|e}}">{{anchor|e}}</a></span>
      {% endfor %}
    {% endif %}

Alternatively you can use the provided `collection` macro as follows:

    {% import 'macros/links.html' as links %}
    <p>Tags: {{ links.collection(tags_links) }}</p>

Since this template variable is generated from the corresponding
attribute name, only use letters and underscores in it. An index
collection can be created for header attributes that contain a list of
string values.

## Document Body {#ref-body}

The remaining part of the document is treated as the content that goes
in the body of the created HTML page. This content can either be written
in [markdown](http://daringfireball.net/projects/markdown/) or marked up
with any HTML tag that can be in the body of an HTML document. The body
format is indicated by the file name extension.

### HTML

    <h1>This is a heading</h1>
    <p>This is a paragraph</p>

### Markdown

    # This is a heading

    This is a paragraph
