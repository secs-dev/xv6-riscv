#!/bin/sh

set -e -x

echo "Installing dependencies"

apt-get update
DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
apt-get install -y build-essential
apt-get install -y gcc-riscv64-unknown-elf
apt-get install -y qemu-system-misc
apt-get install -y vim
apt-get clean
