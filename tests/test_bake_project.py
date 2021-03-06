#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test bake project."""

from contextlib import contextmanager
import shlex
import os
import sys
import subprocess
import datetime
import yaml
import pytest
from cookiecutter.utils import rmtree

from click.testing import CliRunner

if sys.version_info > (3, 0):
    import importlib
else:
    import imp


@contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """Delete the temporal directory that is created when executing the tests.

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its
                    temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """Run a command from inside a given directory, returning the exit status.

    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    """Run a command from inside a given directory."""
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies."""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_year_compute_in_license_file(cookies):
    """Test year compute in license file."""
    # pylint: disable=invalid-name
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(cookies):
    """Test bake with defaults."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'python_boilerplate' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'tests' in found_toplevel_files
        assert 'travis_pypi_setup.py' in found_toplevel_files


def test_bake_and_run_tests(cookies):
    """Test bake and run tests."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir('python setup.py test', str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_withspecialchars_and_run_tests(cookies):
    """Test bake with special characters and run tests.

    Ensure that a `full_name` with double quotes does not break setup.py
    """
    # pylint: disable=invalid-name
    context = {'full_name': 'name "quote" name'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project.isdir()
        assert run_inside_dir('python setup.py test', str(result.project)) == 0


def test_bake_and_run_travis_pypi_setup(cookies):
    """Test bake and run travis pypi setup."""
    # pylint: disable=invalid-name
    with bake_in_temp_dir(cookies) as result:
        project_path = str(result.project)
        travis_setup_cmd = ('python travis_pypi_setup.py'
                            ' --repo napalm255/cookiecutter-pymodule'
                            ' --password invalidpass')
        run_inside_dir(travis_setup_cmd, project_path)
        travis_config = yaml.load(result.project.join(".travis.yml").open())
        min_size_of_encrypted_password = 50
        password_len = len(travis_config["deploy"]["password"]["secure"])
        assert password_len > min_size_of_encrypted_password


def test_bake_without_travis_pypi_setup(cookies):
    """Test bake without travis pypi setup."""
    # pylint: disable=invalid-name
    context = {'use_pypi_deployment_with_travis': 'n'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        travis_config = yaml.load(result.project.join(".travis.yml").open())
        assert "deploy" not in travis_config
        assert "python" in travis_config["language"]
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'travis_pypi_setup.py' not in found_toplevel_files


def test_bake_minimal_files(cookies):
    """Test bake minimal files."""
    context = {'minimal_files': 'y'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'AUTHORS.rst' not in found_toplevel_files
        assert 'CONTRIBUTING.rst' not in found_toplevel_files
        assert 'HISTORY.rst' not in found_toplevel_files
        assert 'MANIFEST.in' not in found_toplevel_files
        assert 'Makefile' not in found_toplevel_files


def test_make_help(cookies):
    """Test make help."""
    with bake_in_temp_dir(cookies) as result:
        output = str(check_output_inside_dir('make help', str(result.project)))
        assert "check code coverage quickly with the default Python" in output


def test_bake_selecting_license(cookies):
    """Test bake selecting license."""
    # pylint: disable=line-too-long
    license_strings = {
        'MIT license': 'MIT ',
        'BSD license': 'Redistributions of source code'
                       ' must retain the above copyright notice, this',
        'ISC license': 'ISC License',
        'Apache Software License 2.0': 'Licensed under the Apache License,'
                                       ' Version 2.0',
        'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license_string, target_string in license_strings.items():
        context = {'open_source_license': license_string}
        with bake_in_temp_dir(cookies, extra_context=context) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license_string in result.project.join('setup.py').read()


def test_bake_not_open_source(cookies):
    """Test bake not open source."""
    context = {'open_source_license': 'Not open source'}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in result.project.join('README.rst').read()


def test_using_pytest(cookies):
    """Test using pytest."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        test_file = result.project.join('tests/test_python_boilerplate.py')
        lines = test_file.readlines()
        assert "import pytest" in ''.join(lines)


def test_project_with_invalid_module_name(cookies):
    """Test project with invalid module name."""
    # pylint: disable=invalid-name
    result = cookies.bake(extra_context={'project_name': 'with-a-dash'})
    assert result.project is None
    result = cookies.bake()
    project_path = str(result.project)

    # when:
    travis_setup_cmd = ('python travis_pypi_setup.py'
                        ' --repo napalm255/cookiecutter-pymodule'
                        ' --password invalidpass')
    run_inside_dir(travis_setup_cmd, project_path)

    # then:
    result_travis_config = yaml.load(open(os.path.join(project_path,
                                                       ".travis.yml")))
    assert "secure" in result_travis_config["deploy"]["password"],\
        "missing password config in .travis.yml"


def test_bake_with_console_script_files(cookies):
    """Test bake with console script files."""
    # pylint: disable=unused-variable, invalid-name
    result = cookies.bake()
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "__main__.py" in found_project_files

    setup_path = os.path.join(project_path, 'setup.py')
    with open(setup_path, 'r') as setup_file:
        assert 'entry_points' in setup_file.read()


@pytest.mark.skip
def test_bake_with_console_script_cli(cookies):
    """Test bake with console script cli."""
    # pylint: disable=unused-variable, invalid-name
    result = cookies.bake()
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, 'python_boilerplate.py')
    module_name = '.'.join([project_slug, 'cli'])
    if sys.version_info >= (3, 5):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cli)
    elif sys.version_info >= (3, 3):
        file_loader = importlib.machinery.SourceFileLoader
        cli = file_loader(module_name, module_path).load_module()
    else:
        cli = imp.load_source(module_name, module_path)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.cli)
    assert noarg_result.exit_code == 0
    noarg_output = ' '.join(['Replace this message by putting your code into',
                             project_slug])
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.cli, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message' in help_result.output
