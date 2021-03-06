=====================
Cookiecutter PyModule
=====================

.. image:: https://img.shields.io/travis/napalm255/cookiecutter-pymodule.svg
    :target: https://travis-ci.org/napalm255/cookiecutter-pymodule
    :alt: Linux build status on Travis CI

.. image:: https://pyup.io/repos/github/napalm255/cookiecutter-pymodule/shield.svg
     :target: https://pyup.io/repos/github/napalm255/cookiecutter-pymodule/
     :alt: Updates

.. image:: https://pyup.io/repos/github/napalm255/cookiecutter-pymodule/python-3-shield.svg
     :target: https://pyup.io/repos/github/napalm255/cookiecutter-pymodule/
     :alt: Python 3

.. image:: https://readthedocs.org/projects/cookiecutter-pymodule/badge/?version=latest
		:target: http://cookiecutter-pymodule.readthedocs.io/en/latest/?badge=latest
		:alt: Documentation Status

Cookiecutter_ template for a Python module.

* GitHub repo: https://github.com/napalm255/cookiecutter-pymodule/
* Documentation: https://cookiecutter-pymodule.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python module project::

    cookiecutter https://github.com/napalm255/cookiecutter-pymodule.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the `cookiecutter-pymodule tutorial`_.

.. _`cookiecutter-pymodule tutorial`: https://cookiecutter-pymodule.readthedocs.io/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Nekroze/cookiecutter-pymodule`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

* `tony/cookiecutter-pymodule-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc conventions.
  See ``README.rst`` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

* `ardydedase/cookiecutter-pymodule`_: A fork with separate requirements files rather than a requirements list in the ``setup.py`` file.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi

.. _`Nekroze/cookiecutter-pymodule`: https://github.com/Nekroze/cookiecutter-pymodule
.. _`tony/cookiecutter-pymodule-pythonic`: https://github.com/tony/cookiecutter-pymodule-pythonic
.. _`ardydedase/cookiecutter-pymodule`: https://github.com/ardydedase/cookiecutter-pymodule
.. _github comparison view: https://github.com/tony/cookiecutter-pymodule-pythonic/compare/napalm255:master...master
.. _`network`: https://github.com/napalm255/cookiecutter-pymodule/network
.. _`family tree`: https://github.com/napalm255/cookiecutter-pymodule/network/members
