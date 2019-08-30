# Problem link: https://w...content-available-to-author-only...t.com/subset-sum-problem/


def subsetSum(A, k, n):
    if k == 0:
        return True
    if n == len(A) or k < 0:
        return False
    include = subsetSum(A, k - A[n], n + 1)
    exclude = subsetSum(A, k, n + 1)
    return include or exclude


def subsetSumDP(A, total):
    m, n = len(A) + 1, total + 1
    cache = [[False for x in range(n)] for x in range(m)]
    for x in range(m):
        cache[x][0] = True
    for i in range(1, m):
        for j in range(1, n):
            if j < A[i - 1]:
                cache[i][j] = cache[i - 1][j]
            else:
                cache[i][j] = cache[i - 1][j] or cache[i - 1][j - A[i - 1]]

    for idx, item in enumerate(cache):
        print(idx, item)
    return cache[m - 1][n - 1]


if __name__ == '__main__':
    # A = [7, 3, 2, 5, 8]
    # k = 18
    A = [2, 3, 5, 6, 8, 10]
    k = 10
    # print(subsetSum(A, k, 0))
    print(subsetSumDP(A, k))
