#!/bin/sh

set -e

cd "$(dirname "$0")"

docker build . -t ghcr.io/vityaman/xv6:latest
