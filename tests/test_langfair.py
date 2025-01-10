import unittest
from langfair import BiasEvaluator

class TestLangFair(unittest.TestCase):
    def test_bias_evaluation(self):
        evaluator = BiasEvaluator(model='test-model')
        prompts = [
            "Test prompt 1.",
            "Test prompt 2."
        ]
        results = evaluator.assess_bias(prompts)
        self.assertIsNotNone(results)
