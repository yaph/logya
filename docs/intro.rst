.. intro:

Introduction
============

You may ask why another static site generator, when there are so many
others? Valid question, simple answer: all the others are doing it
wrong. No, seriously, tools like
`Jekyll <https://github.com/mojombo/jekyll>`_,
`Hyde <http://hyde.github.io/>`_ or
`mynt <http://mynt.uhnomoli.com/>`_ are very powerful and probably
provide more features out of the box than Logya ever will.

Two key differences comparing Logya with the above tools are:

* Content can be written in markdown **and** HTML.
* More flexible site URL structure: the url for each document must be
  specified in the document header and is independent of the file's
  location within the content directory. This way you can freely
  structure your content and choose your preferred style of URLs, e.g.
  ``example.com/path/doc/`` or ``example.com/path/doc.html``.