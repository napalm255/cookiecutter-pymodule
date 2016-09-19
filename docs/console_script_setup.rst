.. _console-script-setup:


Console Script Setup
=================

Included by default.

How It Works
------------

The '__main__.py' is used to enable calling via 'python -m {{ cookiecutter.project_slug }}'.
This file simply imports '{{ cookiecutter.project_slug }}.cli()', where all the real code is located.
An entry point is added to setup.py that points to the main function in __main__.py.

Usage
------------
To use the console script in development:

.. code-block:: bash

    pip install -e projectdir

'projectdir' should be the top level project directory with the setup.py file

The script will be generated with output for no arguments and --help.

--help
    show help menu and exit

Known Issues
------------
Installing the project in a development environment using:

.. code-block:: bash

    python setup.py develop

will not set up the entry point correctly. This is a known issue with Click.
The following will work as expected:

.. code-block:: bash

    python setup.py install
    pip install mypackage

With 'mypackage' adjusted to the specific project.


More Details
------------

You can read more about Click at:
http://click.pocoo.org/
