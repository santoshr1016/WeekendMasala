from functools import reduce


def create_2d_array():
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)


def array_reduction(ll):
    ll.sort()
    print(ll)
    size = len(ll)-1
    res = 0
    i=0
    while i < size:
        res += ll[i]+ll[i+1]
        ll[i] = res
        ll[i+1] = res
        i += 1
    print(ll)
    return ll.pop()

l = [3,2,4,7,5,9]
print(array_reduction(l))
# l = [4, 6, 8]
# print(array_reduction(l))
# l = [1, 2, 3]
# array_reduction(l)

