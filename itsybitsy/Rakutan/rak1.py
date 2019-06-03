def generator(M, N):
    while M <= N:
        yield M
        M += 1


def solution(M, N):
    # write your code in Python 3.6

    result = 0
    for item in generator(M, N):
        result ^= item
    print(result)


def solution2(M, N):
    l = range(M, N+1)
    result = 0
    for item in l:
        result ^= item
    print(result)

#
tc = int(input())
for i in range(tc):
    num = int(input())
    solution2(1, num)

M = 5
N = 12

solution(M, N)
# solution2(M, N)
