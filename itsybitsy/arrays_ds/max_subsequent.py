def find_max_subsequent(arr):
    if not len(arr):
        return
    cur_sum = max_sum = arr[0]
    for item in arr[1:]:
        print(cur_sum)
        cur_sum = max(cur_sum + item, item)
        max_sum = max(cur_sum, max_sum)
    return max_sum

print(find_max_subsequent([10, -32, 5 ,-7, 10, 18, -2]))
