---
page: 2
title: Getting Started
template: page.html
created: 2013-09-08 19:45:45
---
## Create a starter site

    logya create mysite

This command will create a new sub directory in your current working directory called `mysite` containing a starter site.

## Change to the starter site directory

    cd mysite

## Generate files to public

    logya generate

This command generates HTML files from the documents found in the `content` directory and copies static resources to the newly created `public` directory.

## Serve site from public directory

    logya serve

Run this command in the root directory of your `mysite` project and it will serve the static files from the directory `public`. When you edit files in your projects source directory and reload them in the browser they will be updated, so this can be used for live editing your site and see changes immediately.

## Show help

    logya -h

Show the help output of the `logya` command with information on sub commands and options, for help on a sub command call it with the -h option, e.g. `logya create -h`.
