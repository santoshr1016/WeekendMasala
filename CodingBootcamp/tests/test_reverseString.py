from unittest import TestCase
from reverse_string import ReverseString
from nose.tools import assert_equal


class TestReverseString(TestCase):
    def test_reverse_method_1(self):
        fun = ReverseString().reverse_method_1
        assert_equal(fun("Santosh"), "hsotnaS")

    def test_reverse_method_2(self):
        rs = ReverseString()
        assert_equal(rs.reverse_method_2(), "tluafed")


def main():
    test = TestReverseString()
    test.test_reverse_method_1()
    test.test_reverse_method_2()

if __name__ == '__main__':
    main()