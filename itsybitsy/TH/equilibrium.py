def solution(a):
    for idx, item in enumerate(a):
        if sum(a[: idx]) == sum(a[(idx+1):]):
            return idx

    return -1
a = [-1, 3, -4, 5, 1, -6, 2, 1]
solution(a)
