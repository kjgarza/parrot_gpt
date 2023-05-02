import unittest
from abc import ABCMeta
from parrot_gpt.model_interface import ModelInterface

class TestModelInterface(unittest.TestCase):

    class DummyModel(ModelInterface):
        def __init__(self):
            super().__init__()

        def get_model(self):
            pass

        def get_tokenizer(self):
            pass

        def transform_prompt(self, prompt):
            pass

    def setUp(self):
        self.dummy_model = self.DummyModel()

    def test_model_interface_methods(self):
        self.assertTrue(hasattr(self.dummy_model, 'get_model'))
        self.assertTrue(hasattr(self.dummy_model, 'get_tokenizer'))
        self.assertTrue(hasattr(self.dummy_model, 'transform_prompt'))

if __name__ == '__main__':
    unittest.main()
