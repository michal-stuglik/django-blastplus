### django-blastplus

A simple Django app to conduct web-based homology search with blast+.


#### Requirements

1. Blast+
2. Python 3.6+
3. Django 3.0
4. Biopython

#### Install
```bash
pip install -r requirements/base.txt
```


#### Download

![https://landscape.io/github/michal-stuglik/django-blastplus/master](https://landscape.io/github/michal-stuglik/django-blastplus/master/landscape.svg?style=flat "Code Health")
![http://badge.fury.io/py/django-blastplus](https://badge.fury.io/py/django-blastplus.svg)
![https://travis-ci.org/michal-stuglik/django-blastplus](https://travis-ci.org/michal-stuglik/django-blastplus.svg?branch=master "Travis CI")
![https://codeclimate.com/github/michal-stuglik/django-blastplus](https://codeclimate.com/github/michal-stuglik/django-blastplus/badges/gpa.svg "Code Climate")


#### Quick start

##### Add "blastplus" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = (
        'blastplus',
)
```
##### Include the polls URLconf in your project urls.py like this::
```
url(r'^blast/', include('blastplus.urls')),
```
##### You can modify some defaults in blastplus.settings

    - e.g. modify path to nucleotide database::

```
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
```
##### Visit search pages:

- [Blastn](http://127.0.0.1:8000/blast/blastn), [TBlastn](http://127.0.0.1:8000/blast/tblastn), 
[Blastp](http://127.0.0.1:8000/blast/blastp), [Blastx](http://127.0.0.1:8000/blast/blastx)


Example
-------

See our [NewtBase portal](http://newtbase.eko.uj.edu.pl/blast/blastn/) with django-blastplus app inside.
Code [newtbase @ github](https://github.com/michal-stuglik/newtbase)




