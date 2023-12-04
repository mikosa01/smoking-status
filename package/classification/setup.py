#!/usr/bin/env python
# -- coding: utf-8 --

import io
import os
from pathlib import Path

from setuptools import find_packages, setup



NAME = 'classification'
DESCRIPTION = 'Train and deploy classification model.'
URL = 'https://github.com/mikosa01/smoking-status'
EMAIL = 'michaelmerry8@gmail.com'
AUTHOR = 'Michael Okungbowa'
REQUIRES_PYTHON = '>=3.6.0'


def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()




here = os.path.abspath(os.path.dirname("_file_"))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


ROOT_DIR = Path("_file_").resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['_version_'] = _version


setup(
    name=NAME,
    version=about['_version_'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'classification': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
        'Programming Language :: Python :: 3.10'
        'Programming Language :: Python :: 3.11'
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)