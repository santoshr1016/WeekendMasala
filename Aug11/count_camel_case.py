"""
Author: R Santosh
Prob: Return count from camel case string
"""
import re


class SolutionProb1(object):

    def using_re(self, word):
        words = re.findall('[a-zA-Z][^A-Z]*', word)
        print(words)
        return len(words)

    def using_custom_function(self, string):
        pos = [i for i, e in enumerate(string) if e.isupper()]
        words = []
        begin = 0
        for i in pos:
            if len(string[begin:i]) > 0:  # To handle the case of FileToEditor
                words.append(string[begin:i])
            begin = i
        words.append(string[begin:])
        # print(words)
        return len(words)

if __name__ == '__main__':
    solution = SolutionProb1()
    print(solution.using_custom_function(input()))

