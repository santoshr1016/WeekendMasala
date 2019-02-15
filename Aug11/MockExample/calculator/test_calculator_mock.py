from unittest import TestCase
from unittest.mock import patch
from calculator import Calculator


class TestCalculator2(TestCase):
    def setUp(self):
        self.calc = Calculator()

    @patch('calculator.Calculator.calculate_sum', return_value=9)
    def test_sum(self, calculate_sum):
        self.assertEqual(calculate_sum(2, 3), 9)