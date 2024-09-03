#!/bin/sh

set -e -x

echo "Installing dependencies"

apt-get update

DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

apt-get install -y software-properties-common
apt-get install -y wget

wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
add-apt-repository "deb http://apt.llvm.org/noble/ llvm-toolchain-noble-18 main"

apt-get update

apt-get install -y build-essential
apt-get install -y gcc-riscv64-unknown-elf
apt-get install -y binutils-riscv64-unknown-elf
apt-get install -y gdb-multiarch
apt-get install -y qemu-system-misc

apt-get install -y vim
apt-get install -y tmux
apt-get install -y git

apt-get install -y clangd-18
apt-get install -y bear

apt-get clean
