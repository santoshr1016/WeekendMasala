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
    return -1
    # raise Exception("Should never be here.")


def smallest_missing_3(A):
    s = set(A)
    l = len(A) + 1
    low = 0
    for i in range(1, l):
        if i in s:
            if i > low:
                low = i
    return low + 1

# l = [1,2,3,4,6,7,8,9]
l = [0, 10, 2, -10, -20]

print(smallest_missing_3(l))
print(smallest_missing_2(l))
print(smallest_missing_3(l))
