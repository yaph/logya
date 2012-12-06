#!/bin/bash
cd logya/sites/docs
logya gen
mv deploy /tmp/
cd ../../../
git checkout gh-pages
rm -rf *
mv /tmp/deploy/* .
git add .
git commit -am'deploy documentation'
git push
git checkout master
