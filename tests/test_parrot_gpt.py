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

import unittest
from unittest.mock import MagicMock
from parrot_gpt import ParrotGpt
from models.model_interface import ModelInterface

class TestParrotGpt(unittest.TestCase):

    class DummyModel(ModelInterface):
        def get_model(self):
            pass

        def get_tokenizer(self):
            pass

        def transform_prompt(self, prompt):
            pass

    def setUp(self):
        self.dummy_model = self.DummyModel()
        self.parrot_gpt = ParrotGpt(self.dummy_model)

    def test_model_initialization(self):
        self.assertEqual(self.parrot_gpt.model, self.dummy_model)

    def test_serialize(self):
        self.dummy_model.transform_prompt = MagicMock(return_value="transformed prompt")
        self.parrot_gpt._transform_metadata = MagicMock(return_value="transformed metadata")
        input_metadata = "dummy metadata"
        output = self.parrot_gpt.serialize(input_metadata)
        self.dummy_model.transform_prompt.assert_called_once()
        self.parrot_gpt._transform_metadata.assert_called_once()
        self.assertEqual(output, "transformed metadata")

if __name__ == '__main__':
    unittest.main()
