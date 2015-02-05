.. changes:

Changes
=======

3.2.2 to 3.2.3
--------------

* Added default robots.txt to starter site.
* Added datePublished and dateModified schema markup to post and postinfo templates.

3.2.1 to 3.2.2
--------------

* Updated bootstrap, jquery and fontawesome.
* Use updated property for lastmod in xml sitemap.
* Added postinfo template and sample post that displays it.
* Added author setting to site.yaml.
* Added updated property to document header, if not set by author.

3.2.0 to 3.2.1
--------------

* Allow for non-existing body so a doc can only consist of header values.

3.1.0 to 3.2.0
--------------

* Use yaml's CLoader if available. For complex data structures performance gains are huge.
* Added run command.

3.0 to 3.1.0
------------

* Added get_doc template function.

2.3 to 3.0
----------

Logya version 3.0 is not backwards compatible due to changed configuration.

* YAML based site configuration.
* Python 3 compatibility.
* RSS is generated using template that is now included from create command.