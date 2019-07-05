from unittest import TestCase
from nose.tools import assert_equal
from cb_palindrome import Palindrome


class TestPalindrome(TestCase):
    def test_palindrome_method_1(self):
        tp = Palindrome()
        assert_equal(tp.palindrome_method_1("Nayan"), True)

    # def test_palindrome_method_2(self):
    #     self.fail()

def main():
    test = TestPalindrome()
    test.test_palindrome_method_1()
    test.test_palindrome_method_2()

if __name__ == '__main__':
    main()
