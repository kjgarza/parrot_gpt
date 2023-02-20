#!/usr/bin/env python

"""Tests for `parrot_gpt` package."""

import unittest
from parrot_gpt import parrot_gpt

class TestParrot_gpt(unittest.TestCase):
    """Tests for `parrot_gpt` package."""

    def test_000_datacite_to_crossref(self):
        """Test convert metadata file from datacite to crossref schema."""
        metadata_file = "tests/data/datacite.xml"
        initial_schema = "datacite"
        target_schema = "crossref"
        result = parrot_gpt.ParrotGpt().serialize(metadata_file, initial_schema, target_schema)
        assert(result, "tests/data/crossref.xml")

    def test_001_datacite_to_dcat(self):
        """Test convert metadata file from datacite to dcat schema."""
        metadata_file = "tests/data/datacite.xml"
        initial_schema = "datacite"
        target_schema = "dcat"
        result = parrot_gpt.ParrotGpt().serialize(metadata_file, initial_schema, target_schema)
        assert(result, "tests/data/dcat.xml")

    def test_002_datacite_to_dublin_core(self):
        """Test convert metadata file from datacite to dublin core schema."""
        metadata_file = "tests/data/datacite.xml"
        initial_schema = "datacite"
        target_schema = "dublin_core"
        result = parrot_gpt.ParrotGpt().serialize(metadata_file, initial_schema, target_schema)
        assert(result, "tests/data/dublin_core.xml")

    def test_003_datacite_to_oai_dc(self):
        """Test convert metadata file from datacite to oai_dc schema."""
        metadata_file = "tests/data/datacite.xml"
        initial_schema = "datacite"
        target_schema = "oai_dc"
        result = parrot_gpt.ParrotGpt().serialize(metadata_file, initial_schema, target_schema)
        assert(result, "tests/data/oai_dc.xml")
