---
page: 1
title: Installation
template: page.html
created: 2013-09-08 19:45:45
---
Logya is an open source Python application, check out the source code [on Github](https://github.com/yaph/logya). To install Logya with pip from PyPI run:

    sudo pip install logya

If you cloned the repository, you can install Logya from the project's root directory with the following command:

    sudo python setup.py install

I recommend to install Logya in a virtual environment, so you can have different sites that use different Logya versions.

## Recommended Packages

The Logya site configuration and content headers are in YAML format. Since you are free to define arbitrary attributes and values in both cases, the resulting data structures can become quite complex and time-consuming to parse.

Logya tries to use PyYAML's CLoader and CDumper if they are available. If they are not, you can speed up document parsing by installing `libyaml-dev` before you install Logya or more precisely PyYAML. You also need to have `python3-dev` installed.

On Debian based Linux systems like Ubuntu type:

    sudo apt install libyaml-dev python3-dev

For Logya sites with hundreds of content files, that have many header attributes and nested data structures as values, generating will be noticeably faster.
