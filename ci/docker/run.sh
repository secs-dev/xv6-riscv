#!/bin/sh

set -e

cd "$(dirname "$0")"

docker run \
    -it \
    --rm \
    --volume $(pwd)/../..:/xv6 os-xv6-riscv:latest \
    /bin/bash
