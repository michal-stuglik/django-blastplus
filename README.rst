
django-blastplus
================

A simple Django app to conduct web-based homology search with blast+.


Requirements
------------

1. Blast+
2. Python 2.7
3. Django 1.10

::

    pip install django

4. Biopython

::

    pip install biopython


Download
--------

.. image:: https://landscape.io/github/michal-stuglik/django-blastplus/master/landscape.svg?style=flat
   :target: https://landscape.io/github/michal-stuglik/django-blastplus/master
   :alt: Code Health
   
.. image:: https://badge.fury.io/py/django-blastplus.svg
    :target: http://badge.fury.io/py/django-blastplus

.. image:: https://travis-ci.org/michal-stuglik/django-blastplus.svg?branch=master
    :target: https://travis-ci.org/michal-stuglik/django-blastplus
    :alt: Travis CI
    
.. image:: https://codeclimate.com/github/michal-stuglik/django-blastplus/badges/gpa.svg
   :target: https://codeclimate.com/github/michal-stuglik/django-blastplus
   :alt: Code Climate

Get the latest version of django-blastplus from
https://pypi.python.org/pypi/django-blastplus/


Install
-------

Install with pip

::

    pip install django-blastplus

To get the git version do

::

    $ git clone https://github.com/michal-stuglik/django-blastplus.git


Quick start
-----------

1. Add "blastplus" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (

        'blastplus',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^blast/', include('blastplus.urls')),

3. You can modify some defaults in blastplus.settings

- e.g. modify path to nucleotide database::

BLAST_DB_NUCL_LIST = [
    {
        "name": "sample1",
        "path": 'blastplus/sampledata/sample_db1/sample_db',
        "desc": "Sample database 1",
        "annotated": False, },
    {
        "name": "sample2",
        "path": 'blastplus/sampledata/sample_db2/sample_db2',
        "desc": "Sample database 2",
        "annotated": False, },
]

4. Visit search pages:

- Blastn http://127.0.0.1:8000/blast/blastn

- TBlastn http://127.0.0.1:8000/blast/tblastn

- Blastp http://127.0.0.1:8000/blast/blastp

- Blastx http://127.0.0.1:8000/blast/blastx


Example
-------

See our NewtBase portal with django-blastplus app inside

http://newtbase.eko.uj.edu.pl/blast/blastn/


