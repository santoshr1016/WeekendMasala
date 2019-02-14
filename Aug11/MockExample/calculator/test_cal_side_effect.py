from unittest import TestCase
from unittest.mock import patch
from calculator import Calculator


def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b


class TestCalculator(TestCase):
    @patch('calculator.Calculator.calculate_sum', side_effect=mock_sum)
    def test_sum(self, calculate_sum):
        self.assertEqual(calculate_sum(2,3), 5)
        self.assertEqual(calculate_sum(7,3), 10)