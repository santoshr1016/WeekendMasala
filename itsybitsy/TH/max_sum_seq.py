def max_sum_seq(arr):
    cur_max = max_sum = arr[0]
    for key in arr[1:]:
        max_sum = max(max_sum + key, key)
        cur_max = max(cur_max, max_sum)
    return cur_max


print(max_sum_seq([1,2,-1,4,-50,10,10,-10,-7]))
