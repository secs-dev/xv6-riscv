#!/bin/sh

set -e

cd "$(dirname "$0")"

docker run \
    -it \
    --rm \
    --volume $(pwd)/../..:/xv6 vityamand/xv6:latest \
    /bin/bash
