import unittest
from unittest.mock import MagicMock, patch
from parrot_gpt.model_interface import *
from parrot_gpt.prompts import *
from parrot_gpt.exceptions import EmptyMetadataError, UnsupportedSchemaStandard
from parrot_gpt import ParrotGpt


class TestParrotGpt(unittest.TestCase):

    def setUp(self):
        self.model = MagicMock()
        self.parrot_gpt = ParrotGpt(self.model)

    @patch.object(ParrotGpt, 'serialize')
    def test_serialize_enrichment(self, mock_serialize):
        args = MagicMock()
        args.prompt_type = "enrichment"
        args.fair = "FAIR"
        input_metadata = "input_metadata"

        expected_prompt = fair_prompt.format(metadata=input_metadata, fair=args.fair)
        self.model.transform_prompt.return_value = expected_prompt

        self.parrot_gpt.serialize(input_metadata, args)

        mock_serialize.assert_called_with(input_metadata, args)

    @patch.object(ParrotGpt, 'serialize')
    def test_serialize_peer_review(self, mock_serialize):
        args = MagicMock()
        args.prompt_type = "peer_review"
        args.venue = "PLOS Medicine"
        input_metadata = "input_metadata"

        expected_prompt = peer_review_prompt.format(metadata=input_metadata, venue=args.venue)
        self.model.transform_prompt.return_value = expected_prompt

        self.parrot_gpt.serialize(input_metadata, args)

        mock_serialize.assert_called_with(input_metadata, args)

    @patch.object(ParrotGpt, 'serialize')
    def test_serialize_crosswalk(self, mock_serialize):
        args = MagicMock()
        args.prompt_type = "crosswalk"
        args.target_schema = "DCAT-rdf"
        args.initial_schema = "datacite-xml"

        expected_prompt = crosswalk_prompt.format(target_schema=args.target_schema, initial_schema=args.initial_schema)
        self.model.transform_prompt.return_value = expected_prompt

        self.parrot_gpt.serialize("", args)

        mock_serialize.assert_called_with("", args)

    @patch.object(ParrotGpt, 'serialize')
    def test_serialize_schema(self, mock_serialize):
        args = MagicMock()
        args.prompt_type = "other"
        args.target_schema = "DCAT-rdf"
        args.initial_schema = "datacite-xml"
        input_metadata = "input_metadata"

        expected_prompt = schema_prompt.format(metadata=input_metadata, target_schema=args.target_schema, initial_schema=args.initial_schema)
        self.model.transform_prompt.return_value = expected_prompt

        self.parrot_gpt.serialize(input_metadata, args)

        mock_serialize.assert_called_with(input_metadata, args)


if __name__ == '__main__':
    unittest.main()
