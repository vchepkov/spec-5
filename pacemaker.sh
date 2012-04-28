#!/bin/sh

version=Pacemaker-1.0.12
cd pacemaker
git archive --format=tar.gz --prefix=pacemaker/ $version > ~/rpmbuild/SOURCES/pacemaker.tar.gz
git log --pretty="format:%H" -n1 $version > ~/rpmbuild/SOURCES/pacemaker-git-hash
