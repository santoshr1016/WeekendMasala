"""
ip - The lines are printed in reverse order.
op - In the are lines order printed reverse.
"""


def fib(n):
    result = [0, 1]
    for i in range(2, n):
        first = result[i-1]
        second = result[i-2]
        result.append(first + second)

    return result


print(fib(10))
