.. installation:

Installation
============

Logya is an open source Python application, check out the source code `on Github <https://github.com/yaph/logya>`_. To install Logya with pip
run:

::

    sudo pip install logya

If you cloned the repository, you can install Logya from the project's root directory with the following command:

::

    sudo python setup.py install

Recommended Packages
--------------------

The Logya site configuration and content headers are in yaml format. Logya tries to use PyYAML's CDumper and CLoader if they are available, so you can speed up document parsing by installing libyaml-dev. On Debian based Linux systems type:

::

    sudo apt-get install libyaml-dev

If you have Logya sites with hundreds of content files, that use many header attributes and nested data structures as values, generating the sites will be noticeably faster.