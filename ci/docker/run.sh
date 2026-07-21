#!/bin/sh

set -e

cd "$(dirname "$0")"

docker run \
    -it \
    --platform linux/amd64 \
    --rm \
    --volume $(pwd)/../..:/xv6 vityamand/xv6:latest \
    /bin/bash
