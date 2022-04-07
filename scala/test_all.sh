#!/usr/bin/env bash

set -x

for dir in */;
do 
    pushd "${dir}"
    sbt test
    popd
done