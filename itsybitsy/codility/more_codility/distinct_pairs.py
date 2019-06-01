def distinct_pairs(ll, target):
    seen = set()
    res = []
    for item in ll:
        find = target - item
        if find not in seen:
            seen.add(item)
        else:
            res.append((item, find))
    print(res)


ll = [1, 2, 3, 6, 7, 8, 9, 1]
target = 10
print(distinct_pairs(ll, target))