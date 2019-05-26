def sliding_window(nums, k, x):
    size = len(nums) - (k-1)
    for i in range(size):
        if sum(nums[i: i+k]) == x:
            return 1
    return 0

nums = [-1, 3, 2, 1, 7, 9, 8, 12, 14]
k = 3
x = 10
rv = sliding_window(nums, k, x)
print(rv)
