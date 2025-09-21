#!/bin/sh

set -e

cd "$(dirname "$0")"

docker push vityamand/xv6:latest
