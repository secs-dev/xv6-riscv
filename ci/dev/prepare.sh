#!/bin/sh

set -e
K=kernel

cd "$(dirname "$0")"
cd ../..

make clean
bear -- make $K/kernel fs.img
