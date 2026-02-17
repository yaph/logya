---
created: 2020-10-07 01:43:52
description: A static website created with Logya.
pre_render: [body]
tags: [Example, Documentation]
template: page.html
title: Welcome to Logya
---
This is your new static site built with Logya. Edit the content, customize the design, and publish your site.

[TOC]

## Getting Started

Your site is ready to go. Here's what you can do next:

- Edit this page at `content/index.md`
- Customize the design in `static/style.css`
- Add new pages in the `content` directory
- Modify the template in `templates/base.html`

## Typography

Logya uses clean, readable typography with sensible defaults. Headings are properly sized and spaced, paragraphs have comfortable line height, and links are easy to spot.

### Lists

Unordered list:

- First item in an unordered list
- Second item with some longer text to show how wrapping works
- Third item

Ordered list:

1. First numbered item
2. Second numbered item
3. Third numbered item

## Code Examples

Inline code looks like `this`, and code blocks are formatted clearly:

```python
def hello_world():
    print("Welcome to Logya!")
    return True
```

A single line of code:

```
logya serve
```

## Definition Lists

Term One
:   This is the definition of the first term. It provides clear explanation of what the term means.

Term Two
:   This is the definition of the second term. Multiple lines are supported and properly formatted.

## Blockquotes

> This is a blockquote. Use it for highlighting important information, quotes from other sources, or to provide emphasis to specific content.

## Links and More

Learn more about [Logya](https://logya.org) and how to build fast, flexible static sites.

---

## Page Source

Want to see how this page is made? Here's the source:

<pre>
{{ filesource('content/index.md') }}
</pre>