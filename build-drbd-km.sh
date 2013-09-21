#!/bin/bash
SRPMS=$1

set -e

for arch in i386 x86_64
do
  if [ $arch == "i386" ] ; then
    target="--target=i686"
  else
    target=""
  fi
  mock -r epel-5-${arch} --init
  mock -r epel-5-${arch} --install kernel kernel-devel kernel-xen kernel-xen-devel kernel-PAE kernel-PAE-devel
  for kernel in `cd /var/lib/mock/epel-5-${arch}/root/lib/modules; ls -1`
  do
     mock -r epel-5-${arch} $target --no-clean --define="kernelversion $kernel" $SRPMS
  done
done
