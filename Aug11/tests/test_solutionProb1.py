from unittest import TestCase
from nose.tools import assert_equal
from Aug11.count_camel_case import SolutionProb1


class TestSolutionProb1(TestCase):

    def test_case_1(self):
        solution = SolutionProb1()

        string = "saveTheWorld"
        expected = 3
        assert_equal(solution.using_custom_function(string), expected)

    def test_case_2(self):
        solution = SolutionProb1()
        string = "saveTheWorldFromAliens"
        expected = 5
        assert_equal(solution.using_custom_function(string), expected)

    def test_case_3(self):
        solution = SolutionProb1()
        string = "TheWorldFromAliens"
        expected = 4
        assert_equal(solution.using_custom_function(string), expected)


def main():
    test = TestSolutionProb1()
    test.test_case_1()
    test.test_case_2()
    test.test_case_3()


if __name__ == '__main__':
    main()

