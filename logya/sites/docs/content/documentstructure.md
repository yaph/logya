---
page: 4
title: Document Structure
template: page.html
created: 2013-09-08 19:45:45
---
Documents are dived into header and body parts.

[TOC]

## Document Header

    ---
    title: Logya Documentation
    template: page.html
    created: 2012-03-18 13:59:16
    image: /path/to/image.png
    ---

The header is in [YAML](https://yaml.org/) format. It starts and ends with 3 dashes. The header is used for setting document attributes, that can be of arbitrary complexity and are accessible in templates. You can set a meta description, the scripts and stylesheets to include and whatever is useful in your scenario. The following attributes are reserved to have special meanings.

### Special Attributes

#### body

Don't set a `body` attribute in the document header. It will be set to the body of the document automatically. An existing value will be overwritten.

#### template

This is the only required attribute. Set it to the Jinja2 template to use for rendering the document. The template file name has to be specified relative to the `templates` directory.

#### title

Setting a document `title` is highly recommended, but if not present the stem part of the content file name will be set as the document title.

#### url

You can manually set a `url` attribute, which must be unique and can be used to refer to a document in templates. If you omit the `url` it will be created from the file name, e. g. the document in `content/book/chapter-1.html` will get the URL `/book/chapter-1/` with the file extension removed. File extensions are removed from HTML and Markdown files.

#### created

If you specify a `created` datetime, you must use the format `YYYY-MM-DD HH:MM:SS` as shown in the example. Otherwise it will be set to the file modification time. I recommend setting this manually to the date of first publication. When you call the `get_docs` function in templates, by default documents will be sorted by `created` in descending order, so newest documents show up first. This is also the order in which documents appear in automatically created collection pages.

#### updated

The `updated` datetime works like `created` and should show when the document was last edited. This can be useful if you want to highlight an edit, but typically the default value is fine.

#### pre_render

Use `pre_render` to enable the use of Jinja template syntax and documents. A sample use case would be for creating absolute URLs for internal links using the `base_url` setting.

    <a href="{{ base_url }}/path/to/page/">Link text</a>

For this to work you have to set `pre_render` to a list of attribute names. To pre-render the `body` add the following line to the document header.

    pre_render: [body]

## Collections

You can create document collections using content attributes and corresponding settings in `site.yaml`. An example is to categorize content using a `tags` attribute.

    tags: [source code, python, programming]

For each value in `tags` a collection is created, that contains all documents where value appears in the `tags` attribute. For each tag value a page is automatically created where you can show the documents in that collection. The URL of the collection page is created from the collection `path` value in `site.yaml` and the value, e. g. the `source code` collection URL could be `/tag/source-code/`.

For each collection in a document an additional template variable will be available named from the collection name and the suffix `_links`, e. g. `tags_links`. This can be used in templates to create a list of links to the collection pages on a content page.

    <ul>
    {% for url, anchor in tags_links %}
        <li><a href="{{ url }}">{{ anchor }}</a></li>
    {% endfor %}
    </ul>

Only use letters and underscores in the names of collections and set the document attribute to a list of string values.

## Document Body

The part after the second `---` separator is the document `body`. Text written in [Markdown](https://daringfireball.net/projects/markdown/) will be converted to HTML, if the corresponding file name ends with `.md` or `.markdown`.