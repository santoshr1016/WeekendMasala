from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calculate_sum(self):
        answer = self.calc.calculate_sum(2, 4)
        self.assertEqual(answer, 6)
