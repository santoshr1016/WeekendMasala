def print_sum(n):
    if n == 1:
        return 1
    else:
        return n + print_sum(n-1)

n = 5
print(print_sum(n))
