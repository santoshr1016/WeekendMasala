from collections import Counter


def show_list(res, item):
    if len(res) >= 2:
        count = Counter(res)
        for val in count.values():
            if val == item:
                return 1
    return 0


n = int(input())
res = []
for i in range(n):
    ll = [int(i) for i in input().strip().split()]
    query, item = ll[0], ll[1]
    if query == 1:
        res.append(item)
    elif query == 2:
        if item in res:
            res.remove(item)
    else:
        print(show_list(res, item))
