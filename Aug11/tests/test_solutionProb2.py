from unittest import TestCase
from nose.tools import assert_equal
from Aug11.military_time_convertor import SolutionProb2


class TestSolutionProb2(TestCase):
    def test_convert_24hr_military(self):
        solution = SolutionProb2()

        string = "12:00:00AM"
        expected = "00:00:00"
        assert_equal(solution.convert_24hr_military(string), expected)


def main():
    test = TestSolutionProb2()
    test.test_convert_24hr_military()

if __name__ == '__main__':
    main()