#!/bin/sh

set -e

cd "$(dirname "$0")"

docker run \
    -it \
    --rm \
    --volume $(pwd)/../..:/xv6 ghcr.io/vityaman/xv6:latest \
    /bin/bash
