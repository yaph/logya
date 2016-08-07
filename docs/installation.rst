.. installation:

Installation
============

Logya is an open source Python application, check out the source code `on Github <https://github.com/yaph/logya>`_. To install Logya with pip from PyPI run:

::

    sudo pip install logya

If you cloned the repository, you can install Logya from the project's root directory with the following command:

::

    sudo python setup.py install

I recommend to install Logya in a virtual environment, so you can have different sites that use different Logya versions.

Recommended Packages
--------------------

The Logya site configuration and content headers are in YAML format. Since you are free to define arbitrary attributes and values in both cases, the resulting data structures can become quite complex and time-consuming to parse.

Logya tries to use PyYAML's CLoader and CDumper if they are available. If they are not, you can speed up document parsing by installing ``libyaml-dev`` before you install Logya or more precisely PyYAML.

On Debian based Linux systems like Ubuntu type:

::

    sudo apt-get install libyaml-dev

You also need to install ``python-dev`` or ``python3-dev``, if they are not installed.

If you have Logya sites with hundreds of content files, that use many header attributes and nested data structures as values, generating the sites will be noticeably faster.