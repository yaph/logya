.. intro:

Introduction
============

I started working on Logya in need of a tool for creating Web sites with consistent user interfaces, that are edited in a familiar and convenient manner and easy to maintain.

Moreover, I wanted to migrate existing CMS backed sites to static Web sites, while retaining the main "dynamic" features and the URL structure.

There were other site generators, most prominently `Jekyll <https://github.com/mojombo/jekyll>`_, available in 2011, but at that time none seemed to support the flexibility I wanted regarding URLs so Logya was born.

I also wanted to work with a familiar and powerful tech stack, i. e. Python and jinja2 for me. For a quick glance at what can be done with Logya, see the features below.

Features
--------

* Write content in markdown **or** HTML in your favorite editor.
* Define content attributes that can be referred to in templates.
* Create content specific templates using the powerful features of jinja2.
* Migrate WordPress or Drupal sites to fast static sites keeping the URLs.
* Automatic generation of a document index with created directories.
* RSS feed generation for all content and index directories.
* Built-in Web server with info level logging and immediate editing
  feedback in the browser.
* Manage, deploy and backup the site with the tools you know, e.g. fabric, tar,
  rsync, git, mercurial, subversion.
* Structured data markup in starter site.
* Canonical URL as ``canonical`` variable available in all templates.
* Use Jinja2 template tags in content body.
* Disqus integration via templates and configuration.