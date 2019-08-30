from functools import reduce


def multiply_ele(arr):
    mul = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    res = [mul // i for i in arr]
    print(res)





multiply_ele([1, 2, 3, 4])