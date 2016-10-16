#!/usr/bin/env bash

python setup.py bdist_wheel

echo 'copy to repository'
cp dist/django_blastplus-*.whl ~/Dropbox/Public/bin/
