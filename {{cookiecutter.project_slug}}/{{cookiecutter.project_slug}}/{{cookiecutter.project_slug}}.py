#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_name }} module."""

from __future__ import absolute_import, unicode_literals, print_function
import logging
import click
from {{ cookiecutter.project_slug }}.log import configure_logging


@click.command()
def cli(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    logging.debug('Starting "%s"...', __file__)
    click.echo('Replace this message by putting your code into '
               '{{cookiecutter.project_slug}}.cli.main')
    click.echo('See click documentation at http://click.pocoo.org/')


def main():
    """Main entry point."""
    configure_logging(level='DEBUG')
    cli()


if __name__ == "__main__":
    main()
