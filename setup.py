import os

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-blastplus',
    version='3.0.0',
    packages=['blastplus'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to conduct web-based blast+ local alignment search.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/michal-stuglik/django-blastplus',
    author='Michal Stuglik',
    author_email='stuglik@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
