from collections import Counter

def show_list(res, item):
    if len(res) >= 2:
        count = Counter(res)
        for val in count.values():
            if val == item:
                return 1
    return 0

def freqQuery(q):
    res = []
    ans = []
    for ll in q:
        query, item = ll[0], ll[1]
        if query == 1:
            res.append(item)
        elif query == 2:
            if item in res:
                res.remove(item)
        else:
            ans.append(show_list(res, item))
    return ans
