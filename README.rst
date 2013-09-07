Logya README
============

.. image:: https://badge.fury.io/py/logya.png
        :target: http://badge.fury.io/py/logya
.. image:: https://travis-ci.org/yaph/logya.png?branch=master
        :target: https://travis-ci.org/yaph/logya

Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

Please see the `documentation`_ for more information on how to use logya for creating Web sites.

Logya Source Directory Structure
--------------------------------

* logya       all logya source files needed for running
    * ext       extension modules
    * sites     barebone example Web sites
* tests

Known issues in 2.1
----------------------

* version number in 2 places setup.py and logya.version
* python run_tests raises `ImportError: cannot import name TestLogya` when both text_extensions and test_writer tests are imported
* see `GitHub Issues`_

Roadmap
-------

Version 2.2
~~~~~~~~~~~

* additional indexes as setting in site.cfg indexes=['language', 'tool'] parse them in docparser, names of indexes should not be used as directory names too ALTERNATIVE specify tags like tools/d3/ which works already, but creates 2 indexes one in tools/ and one in tools/d3/
* add env var in config to set the evironment, if env is set to `dev` additional values will be read fom site_dev.cfg and override existing ones
* make a useful tags index pages
* make tags dir configurable in site.cfg?
* minify and merge JS files, make this work in serve mode too!!!
    * http://pypi.python.org/pypi/slimit/
    * http://developmentseed.org/blog/2011/09/09/jekyll-github-pages/#can_it_aggregate_css_and_javascript
* Refactor template var setting and getting, fixes are ugly
* Inform users during generate when doc URL is used more the once

Version 2.3
~~~~~~~~~~~

* Extensions API    http://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures/
* provide extension hooks in build_indexes and DocParser
* options to enable and or disable extensions in site configuration
* shared extensions .logya/ext

Further Plans and Ideas
-----------------------

* Create content and templates for XML and HTML sitemaps in base site
* Add `logya ext create EXTNAME` command
* automatic description generation as parser extension
* content snippets that are replaced when generating document

Sites built with logya
----------------------

* http://geeksta.net/
* http://ramiro.org/
* http://exploringdata.github.com/


.. _`documentation`: http://yaph.github.com/logya/
.. _`GitHub Issues`: https://github.com/yaph/logya/issues?state=open