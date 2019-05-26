def smallest_missing(arr):
    sl = sorted(list(set(arr)))
    sl_set = set(sl)
    for item in sl:
        if item + 1 not in sl_set:
            if item <= 0:
                return 1
            else:
                return item + 1


def smallest_missing_2(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item - 1] = True
    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1
    raise Exception("Should never be here.")
    return -1


def smallest_missing_3(A):
    s = set(A)
    l = len(A) + 1
    low = 0
    for i in range(1, l):
        if i in s:
            if i > low:
                low = i
    return low + 1


print(smallest_missing_3([1, 3, 67, 4, 1, 2]))
print(smallest_missing_2([102, 333, 555, 666, 777, 2]))
print(smallest_missing_3([102, 333, 555, 666, 777, 2]))
