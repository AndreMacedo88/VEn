Module for VEnCode-related projects based on FANTOM5 databases
==============================================================

|

.. image:: https://img.shields.io/pypi/v/VEnCode
    :target: https://pypi.org/project/VEnCode/
    :alt: PyPI
.. image:: https://img.shields.io/github/v/release/AndreMacedo88/VEnCode?include_prereleases
    :target: https://github.com/AndreMacedo88/VEnCode/releases
    :alt: GitHub release (latest by date including pre-releases)
.. image:: https://img.shields.io/github/release-date/AndreMacedo88/VEnCode
    :target: https://github.com/AndreMacedo88/VEnCode/releases
    :alt: GitHub Release Date
.. image:: https://travis-ci.com/AndreMacedo88/VEnCode.svg?branch=master
    :target: https://travis-ci.com/AndreMacedo88/VEnCode
.. image:: https://coveralls.io/repos/github/AndreMacedo88/VEnCode/badge.svg?branch=master
    :target: https://coveralls.io/github/AndreMacedo88/VEnCode?branch=master
.. image:: https://img.shields.io/pypi/pyversions/VEnCode
    :target: https://pypi.org/project/VEnCode/
    :alt: PyPI - Python Version
.. image:: https://img.shields.io/github/license/AndreMacedo88/VEnCode
    :target: https://github.com/AndreMacedo88/VEnCode/blob/Stable/LICENSE
    :alt: GitHub
.. image:: https://img.shields.io/github/issues/AndreMacedo88/VEnCode
    :target: https://github.com/AndreMacedo88/VEnCode/issues
    :alt: GitHub issues
.. image:: https://readthedocs.org/projects/vencode/badge/?version=latest
    :target: https://vencode.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

|

This module contains classes and functions that perform intersectional genetics-related operations to find VEnCodes
using any matrix of cell types (columns) vs regulatory elements or markers (rows).

Moreover, it contains particular methods to make use of the databases provided by the `FANTOM5 consortium`_, namely the
CAGE enhancer and transcription start site (TSS) databases.

For more information on the VEnCode technology, please refer to `Macedo and Gontijo, GigaScience, 2020`_.

Getting started
---------------

These instructions are designed to:

- Get you a copy of the project up and running on your local machine for development and testing purposes;
- Install the VEnCode package in your python library environment for use in your projects.

Prerequisites
^^^^^^^^^^^^^

To effectively use this module you will need Python3_ with a few external libraries installed in your machine.
Check the requirements_ file.
If you install the package with pip, it should resolve the library requirements for you.

Optionally, if you want to retrieve VEnCodes using the comprehensive FANTOM5 CAGE-seq data, you will have to download
the unannotated TSS files from `FANTOM5 consortium`_ website.
More specifically, for human, download `this file`_ for promoter analysis, and `this one`_ and the `ID-sample name`_
map for enhancers. Finally, download the `curated sample category file`_.

Those 4 files are enough to find CAGE-based VEnCodes for human.

Installing
^^^^^^^^^^
1. Make sure you have the prerequisites;

If you want to edit the project:

2. Fork `this project`_.

You are now ready to go. Optionally, if you are using the FANTOM5 data instead of your own:

3. Put the missing FANTOM5 prerequisite files (only the large TSS files are missing) in the directory called "Files".

If you are a user:

2. Install VEnCode with pip:

.. code-block:: console

    pip install VEnCode

You are good to go. Optionally, if you are using the FANTOM5 data instead of your own:

3. Put all the FANTOM5 prerequisite files in a directory of your choice and when creating DataTpmFantom5 objects remember to pass the argument:

.. code-block:: python

    files_path = "just put here the path to your file"

Using the module
-----------------
There are several ways to use this module:

1. To develop your own projects, import objects directly from VEnCode using, for example:

.. code-block:: python

    import VEnCode
    object1 = VEnCode.DataTpm(...)
    vencodes = VEnCode.Vencodes(object1, ...)
    vencodes.next(amount=2)
    vencodes.export("vencodes", ...)

- You can see examples of some functions and objects being used at the `VEnCode Capsule`_ hosted in CodeOcean.

2. To run the most relevant scripts, use the utility file process.py, which gives easy access to many scripts, for example:

.. code-block:: console

    python process.py get_vencodes Hepatocyte --algorithm heuristic

3. Run any script by going to the "Scripts" folder inside the package and calling the script individually.

Running the Tests
-----------------
Tests for this module can be run in several ways; some examples:

1. In the command-line:

1.1. Using the `process.py` utility file to run all the tests in one go. This is easily done by running the following
command inside the VEnCode module:

.. code-block:: console

    python process.py run_tests

1.2. Run python's standard module "unittest" in the `tests` directory to run each test individually.
Basic example in command line:

.. code-block:: console

    python -m unittest test_internals

1.3. Another way to run each test individually is to install the nosetests python package and run nosetests in the
`tests` directory. Basic example in command line:

.. code-block:: console

    nosetests test_internals.py

2. By importing the VEnCode module in python:

.. code-block:: python

    from VEnCode import tests
    tests.run_all_tests()

Documentation
-------------

- The documentation on the main methods of this tool can be found in the official `documentation`_.
- To see some of the functions in action, refer to the `VEnCode Capsule`_ hosted at CodeOcean.
- For more examples on how to use this module, we suggest going through the scripts folder inside this projects' python package. There, we take the VEnCode tool functions and methods and apply them, as seen in `Macedo and Gontijo, GigaScience, 2020`_.
- Finally, all the public methods are thoroughly documented in the methods' docstring itself.

Contributing
------------

Please read `CONTRIBUTING.rst`_ for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
----------

We use SemVer_ for versioning. For the versions available, see:

- The `tags on github`_, or
- In PyPi_.

Authors
-------

- `Andre Macedo`_
- `Alisson M. Gontijo`_

See also the list of contributors_ who participated in this project.

License
-------

Refer to the file LICENSE_.

Acknowledgements
----------------
- Integrative Biomedicine Laboratory @ CEDOC, NMS, Lisbon (supported by FCT: UID/Multi/04462/2019; PTDC/MED-NEU/30753/2017; and PTDC/BIA-BID/31071/2017 and FAPESP: 2016/09659-3)
- CEDOC: Chronic Diseases Research Center, Nova Medical School, Lisbon
- The MIT Portugal Program (MITEXPL/BIO/0097/2017)
- LIGA PORTUGUESA CONTRA O CANCRO (LPCC) 2017.
- FCT (IF/00022/2012, SFRH/BD/94931/2013, PTDC/BEXBCM/1370/2014)
- Prof. Dr. Ney Lemke and Ms. Benilde Pondeca for important discussions.

.. Starting hyperlink targets:

.. _FANTOM5 consortium: http://fantom.gsc.riken.jp/5/data/
.. _Macedo and Gontijo, GigaScience, 2020: https://doi.org/10.1093/gigascience/giaa083
.. _this file: https://fantom.gsc.riken.jp/5/datafiles/latest/extra/CAGE_peaks/hg19.cage_peak_phase1and2combined_tpm.osc.txt.gz
.. _this one: https://fantom.gsc.riken.jp/5/datafiles/latest/extra/Enhancers/human_permissive_enhancers_phase_1_and_2_expression_tpm_matrix.txt.gz
.. _ID-sample name: https://fantom.gsc.riken.jp/5/datafiles/latest/extra/Enhancers/Human.sample_name2library_id.txt
.. _curated sample category file: https://github.com/AndreMacedo88/VEnCode/blob/master/VEnCode/Files/sample%20types%20-%20FANTOM5.csv
.. _this project: https://github.com/AndreMacedo88/VEnCode
.. _Python3: https://www.python.org/
.. _requirements: https://github.com/AndreMacedo88/VEnCode/blob/master/requirements.txt
.. _SemVer: https://semver.org/
.. _tags on github: https://github.com/AndreMacedo88/VEnCode/tags
.. _PyPi: https://pypi.org/project/VEnCode/#history
.. _VEnCode Capsule: https://codeocean.com/capsule/7611480/tree
.. _documentation: https://vencode.readthedocs.io/en/latest/index.html
.. _CONTRIBUTING.rst: https://github.com/AndreMacedo88/VEnCode/blob/master/CONTRIBUTING.rst
.. _contributors: https://github.com/AndreMacedo88/VEnCode/graphs/contributors
.. _Andre Macedo: https://github.com/AndreMacedo88
.. _Alisson M. Gontijo: https://github.com/alissongontijo
.. _LICENSE: https://github.com/AndreMacedo88/VEnCode/blob/master/LICENSE
