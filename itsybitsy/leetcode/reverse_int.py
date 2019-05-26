import sys


def reverse(x):
    newnum = 0
    flag = False
    if x < 0:
        flag = True
        x = x * -1
    while x:
        digit = x%10
        x = x // 10
        newnum = newnum*10 + digit
    res = (-1 * newnum) if flag else newnum
    if flag:
        return 0 if res < 2** -31 else res
    else:
        return 0 if res > 2 ** -31 else res


print(reverse(-123))
