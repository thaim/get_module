#!/bin/sh

docker run --rm \
       -v `pwd`/modules:/modules \
       -v `pwd`/modulelist.yml:/etc/modulelist.yml \
       thaim/get_module
