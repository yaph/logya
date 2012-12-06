Logya README
============

Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

Please see the `documentation`_ for more information on how to use logya for creating Web sites.

Logya Source Directory Structure
--------------------------------

* logya       all logya source files needed for running
    * ext       extension modules
    * sites     barebone example Web sites
* tests

Known issues in 2.0
----------------------

* python run_tests raises `ImportError: cannot import name TestLogya` when both text_extensions and test_writer tests are imported

Roadmap
-------

Version 2.1
~~~~~~~~~~~

* additional indexes as setting in site.cfg indexes=['language', 'tool'] parse them in docparser, names of indexes should not be used as directory names too ALTERNATIVE specify tags like tools/d3 which may work already
* add env var in config to set the evironment, if env is set to `dev` additional values will be read fom site_dev.cfg and override existing ones
* make a useful tags index pages
* make tags dir configurable in site.cfg?
* minify and merge JS files
    * http://pypi.python.org/pypi/slimit/
    * http://developmentseed.org/blog/2011/09/09/jekyll-github-pages/#can_it_aggregate_css_and_javascript
* Refactor template var setting and getting, fixes are ugly
* Inform users during generate when doc URL is used more the once

Version 2.2
~~~~~~~~~~~

* Extensions API    http://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures/
* provide extension hooks in build_indexes and DocParser
* options to enable and or disable extensions in site configuration
* shared extensions .logya/ext

Further Plans and Ideas
-----------------------

* Create template library including XML and HTML sitemaps
* Add `logya ext create EXTNAME` command
* automatic description generation as parser extension
* content snippets that are replaced when generating document

Sites built with logya
----------------------

* http://geeksta.net/


.. _`documentation`: http://yaph.github.com/logya/
