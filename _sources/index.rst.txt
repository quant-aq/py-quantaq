.. py-quantaq documentation master file, created by
   sphinx-quickstart on Tue Jun 23 12:57:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

py-quantaq
===========

`py-quantaq` is built to make it easy to access the `QuantAQ <https://quant-aq.com>`_ REST API using Python.
The most recent versions of the library can be found on `PyPI <https://pypi.org/project/py-quantaq/>`_ and
support applications written using Python 3.6 and later.


Install the Library
===================

The easiest way to install the library is from PyPI using `pip`, a package manager for Python:


.. code-block:: shell

   $ pip install [-U] py-quantaq


Or, you can add the library to your project using `poetry`, an alternative python project 
management tool:

.. code-block:: shell

   $ poetry add py-quantaq


You can also clone the repository from `GitHub <https://github.com/quant-aq/py-quantaq/>`_
locally and build from source using poetry:

.. code-block:: shell

   $ git clone https://github.com/quant-aq/py-quantaq.git
   $ cd py-quantaq/
   $ poetry install

   

.. important::

   Both the package you're referencing and any dependencies **must be
   installed**.


Running Tests
==============

Testing is done automagically with each new build. However, you can also run tests 
locally if you have cloned the library. To run tests locally using `pytest`:

.. code-block:: shell

   $ poetry run pytest tests

To run them with coverage:

.. code-block:: shell

   $ poetry run pytest tests --cov=quantaq --cov-report term-missing


Making Contributions
====================

All development takes place on GitHub. Please see the GitHub repository 
for instructions.


Reporting Bugs and Other Issues
===============================

Any bugs, issues, or questions can be reported using the GitHub Issues tracker. Please 
provide as much information as possible that will make it easier to solve/fix the problem. 
Useful information to include would be the operating system, python version, and version 
of the opcsim library as well as any dependencies. If there are issues with graphics, 
screenshots are very helpful!


.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Contents:

   Home <self>
   usage
   api
