Parrot GPT
==========

|PyPI version| |Build Status| |Documentation Status| |Updates|

The Parrot-GPT package provides a Python library that can convert any
bibliographic metadata between different schemas using the OpenAI Large
language models via its API. There is no limitation in the schemas that
can be transformed but currently there a restriction has been included
to input and output schemas.

.. figure:: docs/DALL·E2023-02-19%2022.30.16.png
   :alt: Created with DALL·E, an AI system by OpenAI
   :width: 200px

-  Free software: MIT license
-  Documentation: https://parrot-gpt.readthedocs.io.

Metadata Formats
----------------

============= =======
Schema        Example
============= =======
DATS          -
cff           -
crossref_xml  -
JATS          -
BioSchema     -
Codemeta      -
RIF-CS        -
EDMI          -
DCAT          -
DCAT-AP       -
DataCite      -
DataCite-XML  -
DataCite-JSON -
Crossref      -
schema.org    -
bibtex        -
DC-XML        -
DC-JSON       -
Dublin Core   -
============= =======

Installation
------------

You can install ``parrot_gpt`` with ``pip``:

::

   $ pip install parrot_gpt

Usage from the command line
---------------------------

.. code:: sh

       $ export OPENAI_API_KEY={OPENAI_API_KEY}
       $ parrot_gpt.cli -mf ./path/to/your/filename -i crosssref -t datacite > output

.. |PyPI version| image:: https://img.shields.io/pypi/v/parrot_gpt.svg
   :target: https://pypi.python.org/pypi/parrot_gpt
.. |Build Status| image:: https://img.shields.io/travis/kjgarza/parrot_gpt.svg
   :target: https://travis-ci.com/kjgarza/parrot_gpt
.. |Documentation Status| image:: https://readthedocs.org/projects/parrot-gpt/badge/?version=latest
   :target: https://parrot-gpt.readthedocs.io/en/latest/?version=latest
.. |Updates| image:: https://pyup.io/repos/github/kjgarza/parrot_gpt/shield.svg
   :target: https://pyup.io/repos/github/kjgarza/parrot_gpt/
