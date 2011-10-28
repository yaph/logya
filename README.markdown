Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

# Features
* Create responsive static Web sites
* Built-in Web server with info level logging for immediate editing feedback
* Commands for site creation, generation, and serving
* Automatic index generation in created folders
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

The following folders and files are required for generating a Web site with Logya

* content
* static    TODO make this optional
* templates
* site.cfg

# Roadmap

## Version 0.8

* make logya docs the example site
* move Template class from logya.py to classes that need it?

## Version 0.9

* make distribute work and add to PyPI

## Version 1.0

* rebuild everything :D

## Further Plans

* Add logya extension create name command
* RSS feed generation
* XML and HTML sitemap generation
* minify and concatenate CSS and JS
* configurable plugins
* content snippets that are replaced when generating document
* shared extensions .logya/ext
* shared libraries for extensions .logya/lib
* specify indexes in configuration?
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
