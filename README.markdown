Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

Please see the [documentation](http://yaph.github.com/logya/) for more information on how to use logya for creating Web sites.

# Logya Source Directory Structure
* logya       all logya source files needed for running
    * ext       extension modules
    * sites     barebone example Web sites
* tests

# Known issues in 2.1dev
* python run_tests raises "ImportError: cannot import name TestLogya" when both text_extensions and test_writer tests are imported

# Roadmap

## Version 2.1

* Refactor template var setting and getting, fixes are ugly
* Inform users during generate when doc URL is used more the once
* move common functions to common.py
* provide extension hooks in build_indexes and DocParser

## Version 2.2

* use rst for README?
* move roadmap to docs?
* options to enable and or disable extensions in site configuration
* implement scripts and styles as extensions that process multi value document header fields

## Version 2.3

* XML and HTML sitemap generation as extension

## Version 2.4

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
