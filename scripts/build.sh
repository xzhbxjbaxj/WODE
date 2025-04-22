#!/bin/bash

set -e

KERNEL_VERSION="6.7.4"
CONFIG_FILE="kernel-configs/config-debian-amd64"

mkdir -p output
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-$KERNEL_VERSION.tar.xz
tar -xf linux-$KERNEL_VERSION.tar.xz
cd linux-$KERNEL_VERSION

cp ../$CONFIG_FILE .config
make olddefconfig
make -j$(nproc) deb-pkg LOCALVERSION=-wode BBR_CONG_CONTROL=y

mv ../*.deb ../output/
