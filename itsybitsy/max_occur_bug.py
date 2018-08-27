def solution(M, A):
    N = len(A)
    count = [0] * (M+1)
    max_occurance = 1
    index = -1

    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > max_occurance:
                max_occurance = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]


arr = [1, 2, 3, 3, 1, 3, 1]
print(solution(3, arr), arr)
