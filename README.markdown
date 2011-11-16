Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

# Features
* Create responsive static Web sites
* Built-in Web server with info level logging for immediate editing feedback
* Commands for site creation, generation, and serving
* Automatic generation of document indexes in created directories
* Site configuration

# Requirements
* [Python 2.7](http://python.org/)
* [Jinja2](http://jinja.pocoo.org/)

# Directory Structure

## Logya Source
* logya       all logya source files needed for running
    * ext       extension modules
    * sites     barebone example Web sites
* tests

## Site Source

The following folders and files are recognized when generating a Web site with Logya.

* content - required
* templates - required
* site.cfg - required
* static - optional

# Known issues in 1.1dev
* python run_tests raises "ImportError: cannot import name TestLogya" when both text_extensions and test_writer tests are imported

# Roadmap

## Version 1.1

* move common functions to common.py
* provide extension hooks in build_indexes and DocParser
* add support for default scripts and styles in site configuration
* add tags extension

## Version 1.2

* use rst for README?
* move roadmap to docs?
* options to enable and or disable extensions in site configuration
* implement scripts and styles as extensions that process multi value document header fields

## Version 1.3

* RSS feed generation from indexes as extension
* XML and HTML sitemap generation as extension

## Version 1.4

* Add logya extension create name command
* minify and concatenate CSS and JS

## Further Plans and Ideas

* automatic description generation as parser extension
* menu extension to group docs in menus, e.g. menus: nav, links
* content snippets that are replaced when generating document
* shared extensions .logya/ext
* shared libraries for extensions .logya/lib
* specify indexes in configuration?
* make site.cfg optional?
* Use mongodb and implement the following sub commands:
    * logya import - import documents info database, existing ones that are not older than source file modification will be kept
    * logya refresh - refresh existing deployment, update indexes and recreate updated content
    * logya generate - complete generation of deployment files
    * collections: documents, directories with references to all documents inside
    * example document:
        * filepath /index.html
        * urlpath /index/
        * title "title"
        * tags one two three
        * content "<p>page content</p>"
