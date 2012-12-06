#!/bin/bash
cd logya/sites/docs
logya gen
mv deploy /tmp/
cd ../../../
git checkout gh-pages

