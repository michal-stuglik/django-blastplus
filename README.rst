
django-blastplus
================

A simple Django app to conduct web-based homology search with blast+.


Requirements
------------

1. Blast+
2. Python 2.7
3. Django 1.6-1.8

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

- e.g. modify path to nucleotide database (now as a tuple of dbs)::

    BLAST_DB_NUCL_CHOICE = ((os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db1/sample_db'), "Sample database 1", ),
                        (os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db2/sample_db2'), "Sample database 2", ),)


- e.g. modify path to protein databases::

    BLAST_DB_PROT_CHOICE = ((os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db3_prot/sample_db3_prot'), "Sample database 3 - proteins", ),
                        (os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db4_prot/sample_db4_prot'), "Sample database 4 - proteins", ),)

4. Visit search pages:

- Blastn http://127.0.0.1:8000/blast/blastn

- TBlastn http://127.0.0.1:8000/blast/tblastn

- Blastp http://127.0.0.1:8000/blast/blastp

- Blastx http://127.0.0.1:8000/blast/blastx


Example
-------

See our NewtBase portal with django-blastplus app inside

http://newtbase.eko.uj.edu.pl/blast/blastn/


