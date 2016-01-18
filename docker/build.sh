#!/bin/sh

VERSION=`cat VERSION`

sudo docker build \
     -t thaim/get_module:${VERSION} \
     .
