#!/bin/sh

set -e

cd "$(dirname "$0")"

WORKDIR="$(pwd)"

cd ../..
python3 "$WORKDIR/hash.py"
cd "$WORKDIR"

python3 main.py ${@}
