import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-blastplus',
    version='0.4.0',
    packages=['blastplus'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to conduct web-based blast+ local alignment search.',
    long_description=README,
    url='https://github.com/michal-stuglik/django-blastplus',
    author='Michal Stuglik',
    author_email='stuglik@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
) 
