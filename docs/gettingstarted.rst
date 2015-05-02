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
content directory, indexes for Web site directories, and copies static
resources to the newly created deploy directory.

Serve site from deploy directory:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    logya serve

Run this command in the root directory of your mysite project and it
will serve the static files from the deploy directory. When you edit
files in your projects source directory and reload them in the browser
they will be updated, so this can be used for live editing your site and
see changes immediately.

Run a script in a Logya context:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    logya run script.py

This command allows you to run a Python script in a Logya context, so you
can access Logya object properties and methods.

The example ``site_index.py`` script in the ``scripts`` directory of the starter
site creates an index of all URLs mapped to document objects without the body
and saves it in JSON format to ``static/site_index.json``. To create this index,
run:

::

    logya run scripts/site_index.py

Get help on logya command:
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    logya -h

Show the help output of the logya command with information on sub
commands and options, for help on a sub command call it with the -h
option, e.g. ``logya create -h``.