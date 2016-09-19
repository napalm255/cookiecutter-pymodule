#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pre cookiecutter generation."""
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % MODULE_NAME)

    # exit to cancel project
    sys.exit(1)
