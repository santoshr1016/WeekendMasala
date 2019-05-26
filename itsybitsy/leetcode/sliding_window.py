def sliding_window(nums, k):
    size = len(nums) - (k-1)
    op_list = []
    for i in range(size):
        op_list.append(max(nums[i: i+k]))
    print(op_list)
    return op_list

nums = [1, 3, -1, -3, 5, 3, 6, 7, 7, 8, 1, 34, -9]
k = 3
rv = sliding_window(nums, k)
print(rv)
