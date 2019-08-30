""" This is stack
_______________________
|Base Case hit return 1| 1
|______________________|
|  2 + print_sum(1)    | 2+1
|______________________|
|  3 + print_sum(2)    | 3+2+1
|______________________|
|  4 + print_sum(3)    | 4+3+2+1
|______________________|

"""


def print_sum(n):
    if n == 1:
        return 1
    return n + print_sum(n-1)

n = 4
print(print_sum(n))


def print_fact(n):
    if n == 1:
        return 1
    return n * print_fact(n-1)

n = 4
print(print_fact(n))


def print_fact_tail_recursion(n, result):
    if n == 1:
        return result
    return print_fact_tail_recursion(n-1, result*n)

n = 4
print(print_fact_tail_recursion(n, 1))