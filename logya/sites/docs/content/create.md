---
page: 3
title: Create a Site
template: page.html
created: 2013-09-08 19:45:45
---
The following command creates the directory `mysite` and copies the `base` site files into it.

    logya create mysite

Currently there are two alternatives: the `docs` site, wich you currently read, and `i18n` that serves as a starting point for multilingual sites. You can set it using the `--site` option.

    logya create --site i18n mysite

## Directory Structure

The following directories and files are recognized when generating a website with Logya.

### content (required)

The content directory contains all of the site's documents. Documents can be located in arbitrary sub directories. To be loaded and parsed ascontent a file must end in one of the following extensions: `html`, `htm`, `xml`, `json`, `js`, `css`, `php`, `md`, `markdown`, `txt`.

### templates (required)

The templates directory contains all of the site's Jinja2 templates.

### site.yaml (required)

This file contains the site configuration in YAML format.

### static (optional)

All files and directories inside `static` will be copied to the root directory of the generated site maintaining its file structure. All static resources such as JavaScript, CSS, image, and server configuration files belong here. You can use any tools you like to compile or generate resources from outside directories.
