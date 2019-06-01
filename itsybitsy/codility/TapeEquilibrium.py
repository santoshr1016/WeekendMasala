import sys


def solution(A):
    l = len(A) - 1
    least = sys.maxsize
    print(least)
    for i in range(l):
        diff = abs(sum(A[:i+1]) - sum(A[i+1:]))
        if diff < least:
            least = diff
    return least


def solution2(A):
    diffs = [abs(sum(A[:i]) - sum(A[i:])) for i in range(1, len(A))]
    return min(diffs)

A = [3, 1, 2, 4, 3]
print(solution2(A))