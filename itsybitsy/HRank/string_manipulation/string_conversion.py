def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])
    return res


# print(levenshtein("Python", "Peithen"))
print(levenshtein("cde", "abc"))

from collections import Counter


def delete(a,b):
    c_a = Counter(a)
    c_b = Counter(b)
    c_common = c_b & c_a
    print(c_common)
    return sum(c_a.values()) + sum( c_b.values()) - 2*sum(abs(i) for i in c_common.values())
print(delete("abc", "cde"))

print("####")

def remove_adj(str1):
    size = len(str1)
    tmp = []
    if size == 1:
        return 1
    tmp.append(str1[0])
    count = 0
    for i in range(1, size):
        if str1[i] == tmp[-1]:
            i += 1
            count += 1
        elif str1[i] != tmp[-1]:
            tmp.append(str1[i])
    print(tmp)
    print(count)

"""
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
"""
remove_adj("AAAA")
remove_adj("BBBBB")
remove_adj("ABABABAB")
remove_adj("BABABA")
remove_adj("AAABBB")

