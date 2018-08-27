def find_uniq(arr):
    d = {}
    for num in arr:
        if num in d:
            d[num] = d[num] + 1
        else:
            d[num] = 0
    for k in d:
        if not d[k]:
            return k


def find_uniq_2(arr):
    arr = sorted(arr)
    if arr[0] == arr[1]:
        return max(arr)
    else:
        return min(arr)


def find_uniq_3(arr):
    d = {}
    for i in arr:
        count = d.get(i, 0)
        count += 1
        d[i] = count
    print(d)

print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq_2([1, 1, 1, 2, 1, 1]))
print(find_uniq_3([1, 1, 1, 2, 1, 1, 3,4,3,4,5,5,1,2,3]))
