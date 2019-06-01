def cut_sticks(arr):
    arr.sort()
    size = len(arr)
    i = 0
    res = list()
    res.append(size)
    while i < size:
        stick = 0
        j = i + 1
        while j < size:
            if arr[i] != arr[j]:
                stick += 1
                arr[j] = arr[j] - arr[i]
            else:
                i += 1
            j += 1
        if stick:
            res.append(stick)
        i += 1
    print(res)


arr = [5, 4, 4, 2, 2, 8]
cut_sticks(arr)
