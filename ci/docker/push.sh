#!/bin/sh

set -e

cd "$(dirname "$0")"

docker push vityamand/xv6:latest
docker push ghcr.io/vityaman/xv6:latest