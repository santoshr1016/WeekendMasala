def solution(A):
    # write your code in Python 3.6
    the_set = set(A)
    l = 0
    r = len(A) - 1
    gap = 0
    while l < r:
        if A[l] != A[r]:
            if abs(A[l] - A[r]) not in the_set:
                if r - l > gap:
                    gap = r - l
        # l += 1
        r -= 1
    return gap


A = [1, 4, 7, 3, 3, 5]

print(solution(A))
