def sum_pair(arr, n):
    seen = set()
    out = set()

    for item in arr:
        target = n - item
        if target not in seen:
            seen.add(item)
        else:
            # out.add((min(item, target), max(item, target)))
            out.add((item, n-item))
    return out

arr = [1,2,2,3,4]
n = 4
print(sum_pair(arr, n))