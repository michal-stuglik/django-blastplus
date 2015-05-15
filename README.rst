
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

.. image:: https://pypip.in/v/django-blastplus/badge.png
    :target: https://pypi.python.org/pypi/django-blastplus

.. image:: https://pypip.in/d/django-blastplus/badge.png
    :target: https://pypi.python.org/pypi/django-blastplus


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

- e.g. modify name or path to nucleotide database (now as a tuple of dbs)::

    BLAST_DB_NUCL_CHOICE = ((os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db1/sample_db'), "Sample database 1", ),
                        (os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db2/sample_db2'), "Sample database 2", ),)

4. Visit search pages:

- Blastn http://127.0.0.1:8000/blast/blastn

- TBlastn http://127.0.0.1:8000/blast/tblastn


Example
-------

See our NewtBase portal with django-blastplus app inside

http://newtbase.eko.uj.edu.pl/blast/blastn/


