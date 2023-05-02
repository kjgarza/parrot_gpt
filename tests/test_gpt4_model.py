import unittest
from unittest.mock import MagicMock, patch
from parrot_gpt.model_interface import GPT4Model, ModelInterface

class TestGPT4Model(unittest.TestCase):

    def setUp(self):
        self.gpt4_model = GPT4Model()

    def test_gpt4_model_inherits_model_interface(self):
        self.assertIsInstance(self.gpt4_model, ModelInterface)

    @patch("model_interface.gpt4_model.openai.GPT4")
    def test_get_model(self, mock_gpt4):
        self.gpt4_model.get_model()
        mock_gpt4.from_pretrained.assert_called_once_with("openai-gpt4")

    @patch("model_interface.gpt4_model.openai.GPT4Tokenizer")
    def test_get_tokenizer(self, mock_gpt4_tokenizer):
        self.gpt4_model.get_tokenizer()
        mock_gpt4_tokenizer.from_pretrained.assert_called_once_with("openai-gpt4")

    def test_transform_prompt(self):
        input_prompt = "dummy prompt"
        expected_transformed_prompt = "GPT-4: " + input_prompt
        output = self.gpt4_model.transform_prompt(input_prompt)
        self.assertEqual(output, expected_transformed_prompt)

if __name__ == '__main__':
    unittest.main()
