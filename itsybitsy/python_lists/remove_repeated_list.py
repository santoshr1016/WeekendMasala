"""
Input : [[1], [1, 2], [3, 4, 5], [2, 1]]
Output : [[1], [1, 2], [3, 4, 5]]
"""

def remove_repeated(inp):
    result = []
    my_set = set()
    for item in inp:
        t = tuple(sorted(item))
        if t not in my_set:
            my_set.add(t)
            result.append(item)
    # l = [list(item) for item in result]
    # print(l)
    print(result)


def method_2(inp):
    return list(map(list, set(map(lambda x: tuple(sorted(x)), inp))))


inp = [[1], [1, 2], [3, 4, 5], [2, 1]]
remove_repeated(inp)
inp = [[1], [1, 2], [3, 4, 5], [2, 1], [1,2,3,4]]
print(method_2(inp))
