import math


def find_divisors(n):
    result = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            # If divisors are equal, print only one
            if n / i == i:
                result.append(i)
            else:
                # Otherwise print both
                result.append(i)
                result.append(n // i)
        i += 1
    return len(result)


def check_ops(num, K):
    ops = 0
    while True:
        if find_divisors(num + 1) == K:
            return True, ops + 1, num +1
        elif find_divisors(num + 1) > K:
            return False, ops, num +1
        elif find_divisors(num + 1) < K:
            num += 1
        ops += 1


def check_ops_negative(num, K):
    ops = 0
    while True:
        if find_divisors(num - 1) == K:
            return True, ops - 1
        elif find_divisors(num - 1) > K:
            return False, ops
        elif find_divisors(num - 1) < K:
            num -= 1
        ops += 1

numbers = input().strip().split(" ")
N = int(numbers[0])
K = int(numbers[1])
list_of_numbers = [int(i) for i in input().split()]
list_of_numbers.sort()
print(list_of_numbers)
ops = 0
magical_array = []
for item in list_of_numbers:
    if item < 3:
        ops += 1
    rv = find_divisors(item)
    if rv == 3:
        magical_array.append(item)
        continue
    if len(magical_array) < K:
        flag, val, mag = check_ops(item, K)
        if flag:
            ops = ops + val
            magical_array.append(mag)
        else:
            flag, val, mag = check_ops_negative(item, K)
            if flag:
                ops = ops + val
                magical_array.append(mag)

print(magical_array, ops)
