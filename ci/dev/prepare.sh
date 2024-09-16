#!/bin/sh

set -e

cd "$(dirname "$0")"
cd ../..

make clean
bear -- make $K/kernel fs.img
