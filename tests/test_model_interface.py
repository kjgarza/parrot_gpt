import os
import unittest
from unittest.mock import MagicMock, patch
import openai
from parrot_gpt.model_interface import GPT4Model, GPT3Model


class TestModelInterface(unittest.TestCase):

    def setUp(self):
        self.api_key = "fake_api_key"
        os.environ["OPENAI_API_KEY"] = self.api_key

    @patch("openai.ChatCompletion.create")
    def test_gpt4_model(self, mock_chatcompletion_create):
        gpt4_model = GPT4Model()

        # Test get_model method
        model_params = gpt4_model.get_model()
        self.assertEqual(model_params["model"], "gpt-3.5-turbo")

        # # Test get_tokenizer method
        # tokenizer = gpt4_model.get_tokenizer()
        # mock_from_pretrained.assert_called_with("openai-gpt4")

        # Test transform_prompt method
        prompt = {"system": "System prompt", "user": "User prompt"}
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Transformed prompt"
        mock_chatcompletion_create.return_value = mock_response

        result = gpt4_model.transform_prompt(prompt)
        self.assertEqual(result, "Transformed prompt")
        mock_chatcompletion_create.assert_called_with(model=model_params["model"], messages=[
            {"role": "system", "content": prompt["system"]},
            {"role": "user", "content": prompt["user"]}
        ])

    @patch("openai.Completion.create")
    def test_gpt3_model(self, mock_completion_create):
        gpt3_model = GPT3Model()

        # Test get_model method
        model_params = gpt3_model.get_model()
        self.assertEqual(model_params["model"], "text-davinci-003")

        # # Test get_tokenizer method
        # tokenizer = gpt3_model.get_tokenizer()
        # mock_from_pretrained.assert_called_with("openai-gpt4")

        # Test transform_prompt method
        prompt = {"system": "System prompt", "user": "User prompt"}
        mock_response = MagicMock()
        mock_response.choices[0].text = "Transformed prompt"
        mock_completion_create.return_value = mock_response

        result = gpt3_model.transform_prompt(prompt)
        self.assertEqual(result, "Transformed prompt")
        mock_completion_create.assert_called_with(**model_params, prompt=prompt["user"])


if __name__ == '__main__':
    unittest.main()
