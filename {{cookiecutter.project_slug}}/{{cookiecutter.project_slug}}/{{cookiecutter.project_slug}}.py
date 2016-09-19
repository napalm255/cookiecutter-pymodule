#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_name }} module."""

import click

@click.command()
def cli(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo('Replace this message by putting your code into '
               '{{cookiecutter.project_slug}}.cli.main')
    click.echo('See click documentation at http://click.pocoo.org/')
    click.echo('Arguments: ', args)


if __name__ == "__main__":
    cli()
