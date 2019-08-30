"""
https://www.hackerrank.com/challenges/max-array-sum/problem
Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.

For example, given an array [-2, 1, 3, -4, 5]

Solution : 8

"""


def max_array_sum(lst):
    size = len(lst)
    max_memo = [0]*size
    max_memo[0] = lst[0] if lst[0] > 0 else 0
    max_memo[1] = lst[1] if lst[1] > max_memo[0] else max_memo[0]

    for i in range(2, size):
        max_memo[i] = max(max_memo[i-1], lst[i] + max_memo[i-2])
    return max_memo[size - 1]

# lst = [-2, 1, 3, -4, 5]
lst = [3, 7, 4, 6, 5, 8]
# lst = [3, 5, -7, 8, 10]
print(max_array_sum(lst))

