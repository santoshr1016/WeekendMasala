import re


def all_sub_strings(s1, s2):
    res = [i for i in range(len(s1)) if s1.startswith(s2, i)]
    print(res)
    # s2_size = len(s2)
    # res = [i for i in range(len(s1)) if s1.startswith(s2, i, i+s2_size)]
    # print(res)


def substring(s1, s2):
    print(s1.find(s2))


def using_re(s1, s2):
    print(s1.find(s2))
    res = [i.start() for i in re.finditer(s2, s1)]
    print(res)


str1 = "this is santosh san is the engineer san"
str2 = "san"
all_sub_strings(str1, str2)
substring(str1, str2)
using_re(str1, str2)
