"""
lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
op = [4, -1, 2, 1]
"""


def cubic_solution(lst):
    max_sum_yet = float('-inf')
    size = len(lst)
    for left in range(size):
        for right in range(left, size):
            window_sum = 0
            for i in range(left, right):
                window_sum += lst[i]
            if window_sum > max_sum_yet:
                max_sum_yet = window_sum
    print(max_sum_yet)


def quadratic_solution(lst):
    max_sum_yet = float('-inf')
    size = len(lst)
    for left in range(size):
        window_sum = 0
        for right in range(left, size):
            window_sum += lst[right]
            if window_sum > max_sum_yet:
                max_sum_yet = window_sum
    print(max_sum_yet)


def dp_solution(lst):
    size = len(lst)
    maxSoFar = lst[0]
    maxEndingHere = lst[0]

    for i in range(1, size):
        maxEndingHere = max(lst[i], maxEndingHere + lst[i])
        maxSoFar = max(maxSoFar, maxEndingHere)

    print(maxSoFar)

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cubic_solution(lst)
quadratic_solution(lst)
dp_solution(lst)