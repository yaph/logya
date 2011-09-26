Geeklog is a static Web site generator written in Python designed to be easy
to use and flexible.

# Features
* Create responsive static Web sites
* Built-in Web server with info level logging for immediate editing feedback
* Commands for site creation, generation, and serving

# Requirements
* [Python 2.7](http://python.org/)
* [Jinja2](http://jinja.pocoo.org/)

# Directory Structure

## Geeklog Source
* geeklog       all geeklog source files needed for running
    * ext       extension modules
    * sites     barebone example Web sites
* tests

## Site Source

The following folders and files are required for generating a Web site with Geeklog

* content
* static
* templates
* site.cfg

# Roadmap

## Version 0.5

* site and content configuration
* index generation

## Version 0.6

* make geeklog docs the example site that is created with ./geeklog init example_site

## Version 0.7

* make distribute work

## Further Plans

* RSS feed generation
* XML and HTML sitemap generation
* minify and concatenate CSS and JS
* configurable plugins
* content snippets that are replaced when generating document
