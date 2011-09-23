Geeklog is a static Web site generator written in Python designed to be easy
to use and flexible.

# Features
* Create responsive static Web sites
* Built-in Web server
* Commands for site creation, generation, and serving

# Requirements
* [Python 2.7](http://python.org/)
* [Jinja2](http://jinja.pocoo.org/)

# Directory Structure

## Geeklog Source
* geeklog
    * ext
    * sites
* tests

## Site Source
* content
* static
* templates

## Generated Site
* deploy
    * content
    * static

# Roadmap

## Version 0.4

* site and content configuration

## Version 0.5

* make distribute work

## Version 0.6

* make geeklog docs the example site that is created with ./geeklog init example_site

## Further Plans

* minify and concatenate CSS and JS
* configurable plugins
* XML and HTML sitemap generation
