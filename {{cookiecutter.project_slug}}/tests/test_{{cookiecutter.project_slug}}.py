#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` module."""

import pytest
from contextlib import contextmanager
from click.testing import CliRunner
from {{ cookiecutter.project_slug }}.__main__ import main


class Test{{ cookiecutter.project_slug|title }}(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass


if __name__ == '__main__':
    sys.exit(pytest.main())
