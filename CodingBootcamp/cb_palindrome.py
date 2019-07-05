class Palindrome(object):
    def palindrome_method_1(self, ss="aba"):
        ss = ss.lower()
        return ss == ss[::-1]

    def palindrome_method_2(self, ss="abba"):
        pass


