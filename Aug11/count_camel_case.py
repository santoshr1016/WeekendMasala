"""
Author: R Santosh
Prob: Return count from camel case string
"""
import re


def using_re(word):
    words = re.findall('[a-zA-Z][^A-Z]*', word)
    print(words)
    return len(words)


def using_custom_function(s):
    pos = [i for i, e in enumerate(s) if e.isupper()]
    words = []
    begin = 0
    for i in pos:
        if len(s[begin:i]) > 0:  # To handle the case of FileToEditor
            words.append(s[begin:i])
        begin = i
    words.append(s[begin:])
    # print(words)
    return len(words)


# print(using_re(input()))
print(using_custom_function(input()))
