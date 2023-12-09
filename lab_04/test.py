import unittest
from zpz import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_infix_to_postfix(self):
        input_expression = "3 + 4 * 2 / (1 - 5) ^ 2"
        expected_postfix = "342*15-2^/+"
        self.assertEqual(self.calculator.infix_to_postfix(input_expression), expected_postfix)

    def test_evaluate_postfix(self):
        postfix_expression = "342*15-2^/+"
        expected_result = 3.5 
        self.assertAlmostEqual(self.calculator.evaluate_postfix(postfix_expression), expected_result, places=2)

if __name__ == '__main__':
    unittest.main()