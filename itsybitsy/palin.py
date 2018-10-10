class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        rev = word[::-1]
        return word == rev

print(Palindrome.is_palindrome('Deleveled'))