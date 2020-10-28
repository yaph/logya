---
page: 6
title: Configuration
template: page.html
created: 2013-09-08 19:45:45
pre_render: [body]
---
Below you find an explanation of the sections and settings in the `site.yaml` configuration file.

## site

The settings in the `site` section will be available in all templates. Documents can override settings by using corresponding attributes. For example you could set a default `author` in the `site` section, that can be overridden in documents with a `author` attribute.

## collections

This section allows to define collections for categorizing content via corresponding attributes. The default site defines a `tags` collection.

## extensions

In this section you can set Markdown and Jinja extensions to be used when the document `body` is converted to HTML and the page is rendered.

## languages

The languages section is optional and exists to enable additional features for multilingual sites. Please see [I18N]({{ base_url }}/i18n/) for more information.

## Example Configuration

To give a real world example, this site's configuration is shown below.

```yaml
{{ filesource('site.yaml') }}
```