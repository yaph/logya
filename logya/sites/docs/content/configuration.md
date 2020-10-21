---
page: 6
title: Configuration
template: page.html
created: 2013-09-08 19:45:45
pre_render: [body]
---
Below you find an explanation of the sections and settings in the `site.yaml` configuration file.

## site section

The settings in the `site` section will be available in all templates. Documents can override settings by using corresponding attributes. For example you could set a default `title` in the `site` section, that would be overridden in documents with a `title` attribute.

## collections section

This section allows to define collections for categorizing content via corresponding attributes. The default site defines a `tags` collection.

## extensions section

In this section you can set Markdown extensions to be used when the document `body` is converted to HTML.

## languages section

The languages section is optional and exists to enable additional features for multilingual sites. Please see [I18N]({{ base_url }}/i18n/) for more information.
