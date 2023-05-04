Parrot GPT
==========

|PyPI version| |Build Status| |Documentation Status| |Updates|

Parrot GPT is a Python library that enables you to convert bibliographic
metadata between various schemas using OpenAI’s large language models
through its API. The library is not limited to specific schemas, but
currently, some restrictions apply to input and output schemas.

.. figure:: docs/DALL·E2023-02-19%2022.30.16.png
   :alt: Parrot GPT logo

   Parrot GPT logo

-  License: MIT
-  Documentation: https://parrot-gpt.readthedocs.io

Metadata Formats
----------------

The following table shows some examples of metadata formats supported by
Parrot GPT:

+---------------+
| Schema        |
+===============+
| DATS          |
+---------------+
| cff           |
+---------------+
| crossref_xml  |
+---------------+
| JATS          |
+---------------+
| BioSchema     |
+---------------+
| Codemeta      |
+---------------+
| RIF-CS        |
+---------------+
| EDMI          |
+---------------+
| DCAT          |
+---------------+
| DCAT-AP       |
+---------------+
| DataCite      |
+---------------+
| DataCite-XML  |
+---------------+
| DataCite-JSON |
+---------------+
| Crossref      |
+---------------+
| schema.org    |
+---------------+
| bibtex        |
+---------------+
| DC-XML        |
+---------------+
| DC-JSON       |
+---------------+
| Dublin Core   |
+---------------+

Installation
------------

Install ``parrot_gpt`` using ``pip``:

.. code:: bash

   $ pip install parrot_gpt

Usage
-----

Command Line
~~~~~~~~~~~~

Use the cli.py script to transform metadata using a selected large language model and prompt type. Where:


- MODEL is the large language model to use (e.g., turbo, gpt3)
- PROMPT_TYPE is the type of input prompt (e.g., enrich, translate, crosswalk, peer_review)
- INPUT_FILE is the input metadata file
- OUTPUT_FILE is the output metadata file
- OPTIONS are optional arguments, such as --initial_schema, --target_schema, and --venue (for peer review)

For example:

.. code:: shell
   
   $ export OPENAI_API_KEY={OPENAI_API_KEY}
   $
   $ python -m parrot_gpt.cli --model gpt3 --prompt-type translate --input-file input.xml --output-file output.json --initial_schema crossref --target_schema datacite


Python API
~~~~~~~~~~

You can also use Parrot GPT in your Python code:

.. code:: python

   from parrot_gpt import ParrotGpt
   from parrot_gpt.model_interface import GPT3Model
   from collections import namedtuple

   Arguments = namedtuple('Arguments', 'prompt_type initial_schema target_schema')
   args = Arguments(prompt_type="translate", initial_schema="crossref", target_schema="datacite")
   input_metadata= "path/to/your/input_file"

   parrot_gpt = ParrotGpt(GPT3Model())
   output = parrot_gpt.serialize(input_metadata, args)
   print(output)




Models and Prompts
------------

The following large language models are supported:

- turbo: GPT-3.5 Model
- gpt3: GPT-3 Model

The following prompt types are supported:

- enrich: Enriches the input metadata file
- translate: Translates the metadata file to another schema
- crosswalk: Generates a crosswalk between two schemas
- peer_review: Generates a peer review report for the input file

Contributing
------------

Contributions are welcome! Please check the
`issues <https://github.com/kjgarza/parrot_gpt/issues>`__ page for any
existing discussions, or create a new one if you have any suggestions or
ideas.

License
-------

This project is licensed under the MIT License. See the
`LICENSE <LICENSE>`__ file for details.

.. |PyPI version| image:: https://img.shields.io/pypi/v/parrot_gpt.svg
.. |Build Status| image:: https://img.shields.io/travis/kjgarza/parrot_gpt.svg
.. |Documentation Status| image:: https://readthedocs.org/projects/parrot-gpt/badge/?version=latest
.. |Updates| image:: https://pyup.io/repos/github/kjgarza/parrot_gpt/shield.svg

