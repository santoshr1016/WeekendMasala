from collections import OrderedDict

def compress(s):
    count = 1
    size = len(s)
    i = 0
    while i < size:
        if s[i] == s[i+1]:
            count += 1
        else:
            print(s[i], count)
            count = 1
        i += 1
        if i == size -1:
            print(s[i], count)
            break


def compress2(s):
    od = OrderedDict()
    for item in s:
        od[item] = od.get(item, 0) + 1
    print(od)
compress2("AsssDD")