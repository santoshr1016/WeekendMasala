memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = n if n < 2 else fib(n - 2) + fib(n - 1)
    return memo[n]


def solution(N):
    val = fib(N)
    print(val)
    if val > 999999:
        return str(val)[-6:].zfill(6)
    else:
        return str(val).zfill(6)


print(solution(36))
