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

The following folders and files are recognized when generating a Web site with Logya.

* content - required
* templates - required
* site.cfg - required   TODO make this optional?
* static -optional

# Roadmap

## Version 0.9

* add package data http://packages.python.org/distribute/setuptools.html#including-data-files
* http://packages.python.org/distribute/setuptools.html#accessing-data-files-at-runtime
* http://peak.telecommunity.com/DevCenter/PythonEggs#accessing-package-resources
* make distribute work and 

## Version 1.0

* documentation
* replace 0.9
* add to PyPI

## Further Plans and Ideas

* Add logya extension create name command
* RSS feed generation
* XML and HTML sitemap generation
* minify and concatenate CSS and JS
* configurable extensions
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
