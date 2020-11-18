---
page: 5
title: Templates
template: page.html
created: 2013-09-08 19:45:45
---
The template engine that comes with Logya is [Jinja2](http://jinja.pocoo.org/). In addition to the many functions and filters Jinja2 provides you can use the following filters and global functions.

## Filters

### alpha_index

This filter returns an alphabetical index for a list of dictionaries. The `sort_attr` argument specifies what value to use for sorting, it defaults to `title`. You can set `non_ascii_key` to group items, where the value does not start with an ASCII letter. The default `sort_order` is `ascending`.

An example of `alpha_index` in use can be seen on [this page](https://ukealong.com/chords/). The template code looks as follows:

    {% set index = get_collection('chords).index.values()|alpha_index() %}

It gets the list of documents in the `chords` collection index and applies the filter on this list.

### attr_contains

The `attr_contains` filter returns a list of documents that have the given attribute and its value contains the given test value. Consider the following [real world usage example](https://ukealong.com/video/zwC4bGMOkzk/):

    {% set related = get_docs('/video/')|attr_contains('songs', songs[0]) %}

This template snippet first gets documents with a URL that start with `/video/` and then applies the `attr_contains` filter. In this example `songs` is a list and the first item is the song played in the video. You can also check whether a value is `in` other Python sequence types, such as strings.

## Functions

### filesource

You can use the `filesource` function to include the text of an external file on a page. The optional `limit` parameter specifies how many lines to include. If not provided the whole file will be included. The file content is escaped by default, so that you can display HTML or other source code. The example below is taken from the [d3.geomap documentation](http://d3-geomap.github.io/).

    {{ filesource('static/html/d3.geomap.html') }}
    {{ filesource('static/js/maps/world-plain.js') }}

The file is located relative to the site's root directory. This function is mainly intended for documentation purposes as it allows you to include the same source code that is used to render an example visible on the current page. Restricting the number of lines works as follows.

    {{ filesource('path/to/file', lines=6) }}

To not escape the content, you can set raw to True.

    {{ filesource(data, raw=True) }}

This can be used for example to inline SVG code when using SVG sprites.

### get_collection

Call this function with a collection name as defined in your settings to get a dictionary representing that collection. The `index` of a collection is a mapping of URLs to the corresponding collection's meta data and the list of documents contained within it, accessible via the `docs` attribute.

### get_doc

You can use the `get_doc` function to get a document object via its URL, which allows you to create links between documents. Say document A has a `link` property set to the URL of document B. You can then get an object representing B and link to it from within A's template like so:

    {% set B = get_doc(link) %}
    <a href="{{ B.url }}">{{ B.title }}</a>

### get_docs

Use `get_docs` to retrieve a list of documents. If you specify a `url` only documents are included, that start with a URL that starts with the given value. By default documents are sorted by the `created` datetime in `descending` order. YOu can change that behavior via the `sort_attr` and `sort_attr` keyword arguments.
