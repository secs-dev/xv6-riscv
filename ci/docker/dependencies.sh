#!/bin/sh

set -e -x

echo "Installing dependencies"

apt-get update

DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

apt-get install -y software-properties-common wget

wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
./llvm.sh 22

add-apt-repository universe
apt-get update

apt-get install -y \
    build-essential \
    bc \
    gcc-riscv64-unknown-elf \
    binutils-riscv64-unknown-elf \
    gdb-multiarch \
    qemu-system-riscv-hwe \
    opensbi \
    u-boot-qemu \
    \
    vim \
    tmux \
    git \
    \
    clang-format-22 \
    clang-tidy-22 \
    clangd-22 \
    bear

apt-get clean
