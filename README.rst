Logya README
============

.. image:: https://badge.fury.io/py/logya.png
        :target: https://pypi.org/project/logya/
.. image:: https://travis-ci.org/yaph/logya.png?branch=master
        :target: https://travis-ci.org/yaph/logya
.. image:: https://landscape.io/github/yaph/logya/master/landscape.png
        :target: https://landscape.io/github/yaph/logya

Logya is a static Web site generator written in Python designed to be easy
to use and flexible.

Quickstart
----------

::

    # install logya and required packages
    pip install logya

    # create a barebone site
    logya create mysite
    cd mysite

    # add content and then generate the site in the deploy directory
    logya gen

    # serve the site from deploy on http://localhost:8080
    logya serve


Please see the `documentation`_ for more information on how to use logya for
creating Web sites.

Sites built with logya
----------------------

* http://ramiro.org/
* https://geeksta.net/
* https://www.linux-netbook.com/
* https://strahlungsarmehandys.com/
* https://exploring-data.com/
* https://d3-geomap.github.io/
* https://guitarstreams.com/

.. _`documentation`: http://ramiro.org/logya/docs/
.. _`GitHub Issues`: https://github.com/yaph/logya/issues