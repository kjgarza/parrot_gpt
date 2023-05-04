import unittest
from unittest.mock import MagicMock, patch
from parrot_gpt import ParrotGpt
from parrot_gpt.model_interface import ModelInterface
import parrot_gpt.cli

class TestCLI(unittest.TestCase):

    class DummyModel(ModelInterface):
        def get_model(self):
            pass

        def get_tokenizer(self):
            pass

        def transform_prompt(self, prompt):
            pass

    @patch("cli.ArgumentParser.parse_args")
    @patch("cli.ParrotGpt")
    def test_main(self, mock_parrot_gpt, mock_parse_args):
        dummy_model = self.DummyModel()
        mock_parse_args.return_value = MagicMock(
              model="gpt3", 
              prompt_type="", 
              initial_schema="datacite-xml", 
              target_schema="crossref-xml", 
              input_file="distribution.xml", 
              output_file="output.rdf"
        )
        parrot_gpt.cli.MODEL_MAPPING = {"gpt3": dummy_model}

        with patch("builtins.open", unittest.mock.mock_open(read_data="dummy metadata")) as mock_input_file:
            parrot_gpt.cli.main()

        mock_parrot_gpt.assert_called_once_with(dummy_model)
        mock_parrot_gpt.return_value.serialize.assert_called_once_with("dummy metadata")
        mock_input_file.assert_called_once_with("input.txt", "r")
        mock_input_file().write.assert_called_once_with("dummy metadata")

if __name__ == '__main__':
    unittest.main()
