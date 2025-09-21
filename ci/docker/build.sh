#!/bin/sh

set -e

cd "$(dirname "$0")"

docker build . -t vityamand/xv6:latest
