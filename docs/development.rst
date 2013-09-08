.. development:

Development
===========

Tips
----

The following tips are intended for people developing logya application
code.

Create a command that points to the development source:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    ln -s $HOME/code/logya/logya/main.py $HOME/bin/logyadev

This creates a symbolic link in your home bin directory to access logya
commands from your development source, assuming it resides in the first
directory specified above. To not override the logya command from your
installation the command is called logyadev.