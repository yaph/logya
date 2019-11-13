.. gettingstarted:

Getting Started
===============

Create a starter site:
~~~~~~~~~~~~~~~~~~~~~~

::

    logya create mysite

This command will create a new sub directory in your current working
directory called mysite, that includes the resources for a logya starter
site.

Change to the starter site directory:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    cd mysite

Generate files to deploy:
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    logya generate

This command generates HTML files from the documents found in the
content directory, collections for Web site directories, and copies static
resources to the newly created deploy directory.

Serve site from deploy directory:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    logya serve

Run this command in the root directory of your ``mysite`` project and it
will serve the static files from the deploy directory. When you edit
files in your projects source directory and reload them in the browser
they will be updated, so this can be used for live editing your site and
see changes immediately.

Show help
~~~~~~~~~

::

    logya -h

Show the help output of the ``logya`` command with information on sub
commands and options, for help on a sub command call it with the -h
option, e.g. ``logya create -h``.
