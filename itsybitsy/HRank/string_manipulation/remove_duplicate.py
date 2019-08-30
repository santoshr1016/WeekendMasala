"""
ip - tree traversal
op - tre avsl
"""


def print_char(s):
    seen = set()
    for ch in s:
        if ch not in seen:
            yield ch
            seen.add(ch)


def remove_duplicate(str1):
    for i in print_char(str1):
        print(i)



remove_duplicate("tree traversal")