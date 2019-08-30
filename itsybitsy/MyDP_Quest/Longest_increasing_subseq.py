"""
Longest Increasing Subsequence (11, 23, 37)
nums = [11, 23, 10, 37, 21]
"""


def longest_inc_subseq(nums):
    size = len(nums)
    lic = [1] * size
    for i in range(1,size):
        for j in range(i):
            if nums[i] > nums[j] and (lic[i] < lic[j] + 1):
                lic[i] = lic[j] + 1
    max_len = 0
    for i in range(size):
        if max_len < lic[i]:
            max_len = lic[i]
    print(lic)
    return max_len


nums = [11, 23, 10, 37, 21, 50, 80]
print(longest_inc_subseq(nums))
