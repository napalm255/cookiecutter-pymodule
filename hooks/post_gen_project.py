#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Post cookiecutter generation."""
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove file."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        remove_file(os.path.join('{{ cookiecutter.project_slug }}', 'cli.py'))

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
