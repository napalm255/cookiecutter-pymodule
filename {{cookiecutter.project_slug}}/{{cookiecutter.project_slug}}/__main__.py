#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main entry point."""

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def main():
    """Main entry point.

    Run CLI from {{ cookiecutter.project_slug }}
    """
    {{cookiecutter.project_slug}}.main()


if __name__ == "__main__":
    main()
