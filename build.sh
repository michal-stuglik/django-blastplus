#!/usr/bin/env bash

python3 setup.py sdist bdist_wheel

echo 'copy to repository'
cp dist/django_blastplus-*.whl ~/Dropbox/Public/bin/
