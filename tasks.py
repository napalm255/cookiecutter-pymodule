#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke Tasks."""

from __future__ import absolute_import, print_function
import sys
import re
from invoke import task, run
from invoke.exceptions import Failure

COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_NONE = '\033[0m'
MSG_OKAY = '%s[OK]%s' % (COLOR_GREEN, COLOR_NONE)
MSG_FAIL = '%s[FAIL]%s' % (COLOR_RED, COLOR_NONE)


def status(msg, end=False, length=80):
    """Print status message."""
    suffix = '.'*(length-len(msg)) if not end else '\n'
    sys.stdout.write("%s%s" % (msg, suffix))
    sys.stdout.flush()


@task
def bake(ctx):
    """Generate project using defaults."""
    status('Baking project using defaults from cookiecutter.json.')
    result = ctx.run('cookiecutter --no-input . --overwrite-if-exists',
                     warn=True)
    if result:
        status(MSG_OKAY, True)
    else:
        status(MSG_FAIL, True)


@task
def test(ctx, hide=True):
    """Run pytest."""
    length = 80
    if not hide:
        result = ctx.run("py.test --collect-only", hide=True, warn=True)
        match = re.search('collected ([0-9]*).*', result.stdout)
        num_test = int(match.group(1))
        length = 80-num_test
    status('Running pytest.', length=length)
    result = ctx.run('py.test -q --color=yes', hide=hide, warn=True)
    if result:
        status(MSG_OKAY, True)
    else:
        status(MSG_FAIL, True)
