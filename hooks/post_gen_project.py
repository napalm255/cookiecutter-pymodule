#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Post cookiecutter generation."""
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_dir(filepath):
    """Remove file."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_file(filepath):
    """Remove file."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.minimal_files }}' != 'n':
        remove_file('AUTHORS.rst')
        remove_file('CONTRIBUTING.rst')
        remove_file('HISTORY.rst')
        remove_file('MANIFEST.in')
        remove_file('Makefile')
        remove_file('authors_setup.py')
        remove_dir('docs/')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
