---
page: 10
title: Changelog
template: page.html
created: 2013-09-08 19:45:45
---
## 5.2.1

* Fix escaping of HTML in content by turning off Jinja autoescape.

## 5.2.0

* Use pyproject.toml instead of setup.py.
* Update dependencies and don't pin specific versions.

## 5.1.0

* Make `util.slugify` available to templates.

## 5.0.0

This release includes several backwards incompatible changes, most notably it requires Python 3.8 or higher.

* Rename the `deploy` directory to `public` and the attribute `dir_deploy` to `dir_public`.
* Only rebuilt the index in serve mode when a requested URL is not in the index.
* Load site settings once during initialization. Changes to `site.yaml` are visible only after restarting the server.
* The template to use for a file in content must be specified as the header attribute `template`.
* Markdown extensions are configurable in site.yaml. By default no extensions will be used.
* Pre-render content attributes on demand by setting the `pre_render` document attribute to a list of attribute names.
* Removed `canonical` template variable.
* The `languages` setting for multilingual sites and the auto-prefixing of collection URLs with language codes changed.

## 4.7.2

* Allow for header attribute values to contain `---` without breaking the parser.

## 4.7.1

* Only build index for directory and HTML page requests on serve mode.

## 4.7.0

The last release in the 4.x series that adds new features.

* Call strip on given path first in `slugify`.
* Add `doc_index` function in `template.py`.
* Add `collection_index` function in `template.py`.

## 4.6.0

* Make collections available to templates as lists of path, value tuples.
* Convert `created` and `updated` document attributes to datetime objects if they are strings.

## 4.5.0

* Add support for multilingual indexes and add sample `i18n` site.
* Remove support for Python 3.4 as latest Markdown requires at least Python 3.5.

## 4.4.0

* Add `build` and `write` methods to Generate class, so subclasses can easily overwrite the build and write steps.
* Handle UnicodeDecodeError in filesource when reading binary files.
* Make `slugify` function from path module available in templates.

## 4.3.0

* Add `--site` option to choose the base site to use when creating a new one.
* Add `bare` base site with minimal markup and files.

## 4.2.0

* Add attr_contains template filter to enable filtering docs with an attribute containing a given value.
* URL unquote file names so special characters can be used in URLs.

## 4.1.0

* Enable expression-statement extension that adds the do tag.
* Added raw keyword argument to filesource function, which defaults to False.
* Added keep option for `generate` command, which does not remove an existing deploy directory.
* Load newer versions of bootstrap, fontawesome and jquery via CDN.
* Set meta noindex,follow for index pages in starter site.
* Don't write __index__ dir and docs to deploy directory.
* Enable with statement for nested variable scopes in templates.
* Added get_index_template method to core.
* Don't allow for duplicate docs in collections.
* Added parent_paths to path module.
* Renamed collection_paths to collection_index.
* Renamed path.list_dirs_from_url to path.parent_dirs.
* Removed useless list calls.
* Bugfix: don't use str.format to avoid UnicodeEncodeException in Python 2.7.

## 4.0.0

The 4.0.0 release includes several backwards incompatible changes, that affect external scripts that access Logya attributes, as well as RSS and index templates.

* Removed server.log file, log to default stream instead.
* Added option to trim whitespace in templates.
* Set canonical meta tag for index pages.
* Converted allowed_exts from tuple to set.
* Enable attr_list, def_list and fenced_code markdown extensions.
* Enable break and continue in templates.
* Better error message when reading files fails
* Added encode_content function in writer module.
* Renamed docs_parsed to docs.
* Enable configuration of index templates.
* Restructured site configuration.
* Renamed indexes to index/docs/collections.
* Removed all_vars and doc_vars from Template.
* Removed Config class, the config module now consists of load and search_dict_list functions.
* More structured data markup in starter site.
* More comprehensive and updated documentation.
* Removed run command, import Logya in custom scripts instead.
* Removed automatic execution of scripts in bin directory.
* Renamed logya.dir_current to logya.dir_site.
* Renamed logya.dir_dst to logya.dir_deploy.
* Removed FileWriter class entirely.
* Moved canonical_filename to path module.
* Set feed limit in rss template so user can set this to a preferred value.
* Updated dependencies.

## 3.3.0

* More pythonic and readable code.
* Use tox for running tests against different python versions.
* Issue \#58: header attribute url is now optional and will be set from file name if not present.
* Added path module and tests for it.
* Made logya run Python3 compatible.
* Fixed \#52: Removed ext and test.py and code that referenced them.
* Fixed \#48: Use .htaccess from HTML5 Boilerplate.
* New style string formatting.
* Added tests for docparser and docreader modules.
* More appropriate function names.
* Use fontawesome icons for reddit and stumbleupon.
* Fixed \#39: added sample video macro.
* Updated bootstrap.
* Better documentation of filesource template function.
* Write count of generated documents and indexes in verbose mode of generate command, not individual index file names.
* Added default robots.txt to starter site.
* Added datePublished and dateModified schema markup to post and postinfo templates.

## 3.2.2

* Updated bootstrap, jquery and fontawesome.
* Use updated property for lastmod in xml sitemap.
* Added postinfo template and sample post that displays it.
* Added author setting to site.yaml.
* Added updated property to document header, if not set by author.

## 3.2.1

* Allow for non-existing body so a doc can only consist of header values.

## 3.2.0

* Use yaml's CLoader if available. For complex data structures performance gains are huge.
* Added run command.

## 3.1.0

* Added get_doc template function.

## 3.0

Logya version 3.0 is not backwards compatible due to changed configuration.

* YAML based site configuration.
* Python 3 compatibility.
* RSS is generated using template that is now included from create command.
