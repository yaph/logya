.. recipes:

Recipes
=======

Conditional Comments in Documents
---------------------------------

Add a document header field ``comments`` and give it a value to enable
comments for a document:

::

    comments: 1

If you don't want comments on particular posts just omit the
``comments`` header field or don't give it a value:

::

    comments:

In the document's template check for the value of the ``comments`` field
and add the code for an external comment systems like Disqus or Facebook
comments:

::

    {% if comments %}
        comments go here
    {% endif %}

The above code checks that the ``comments`` variable exists and has a
value, so this will also show the comments section if you enter a value
of 0 in the document header.