def exp(x, n):
    if n == 1:
        return x
    if n % 2:
        return x * exp(x * x, n // 2)
    return exp(x * x, n // 2)


print(exp(2, 10))
