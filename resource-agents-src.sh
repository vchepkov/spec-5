#!/bin/sh

version=v3.9.4
cd $HOME/src/resource-agents
git archive --format=tar.gz --prefix=resource-agents/ $version > ~/rpmbuild/SOURCES/resource-agents.tar.gz
