---
page: 8
title: Recipes
template: page.html
created: 2013-09-08 19:45:45
---
This page shows example solutions for common problems. Note that attributes like `comments` and `ignore` don't have a special meaning in Logya until you make them special.

[TOC]

## Conditional Comments

Add a document attribute `comments` and give it a truthy value to enable comments for a document:

    comments: 1

If you don't want comments on particular posts omit the `comments` attribute or give it falsy a value:

    comments: 0

In the document's template check for the value of the `comments` field and add the code for an external comment system:

    {% if comments %}
        Include external comments script here
    {% endif %}

## Ignore Documents in Listings

Usually you don't want the front page of a website or the contact form to appear in listings like an RSS feed. Use a document attribute such as `ignore` and set it to a truthy value and reject these documents in templates:

    {% set docs = get_docs()|rejectattr('ignore') %}

You can the iterate over `docs` without encountering those with the `ignore` attribute.

### Setting Content Files in a Directory to `ignore`

To set all files in a given directory recursively, you can use the following command:

    find content/lesson/ -type f -exec perl -i -pe "BEGIN{undef $/;} s/\-\-\-\n/---\nignore: 1\n/s" {} \;
