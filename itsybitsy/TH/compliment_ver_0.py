from collections import defaultdict

def_dict = defaultdict(list)


def pre_process(arr):
    for idx, item in enumerate(arr):
        if def_dict.get(item):
            def_dict.get(item).append(idx)
        else:
            def_dict[item] = [idx]

arr = [1, 8, -3, 0, 1, 3, -2, 4, 5]
pre_process(arr)

count = 0
n = 6
for key, val in def_dict.items():
    if n-key in def_dict:
        for v in val:
            count = count + len(def_dict.get(n-key))
            # print(count)
            # print(v, def_dict.get(n-key))
print(count)



