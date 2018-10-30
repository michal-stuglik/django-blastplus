#!/usr/bin/env bash

python3 setup.py sdist bdist_wheel

echo 'copy to repository'
cp dist/django_blastplus-*.whl ~/Dropbox/Public/bin/

# upload to repository
# https://github.com/fhamborg/news-please/wiki/PyPI---How-to-upload-a-new-version
# python setup.py sdist upload