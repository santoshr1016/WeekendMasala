# Sample Input
#
# 10
# 7 12 8 12 8 13 8 13 7 13
#
# Sample Output
#
# 4
# 7 12 8 13
# arr = map(int, [item for item in input().strip().split()])
# print(list(arr))
# n = int(input())
# arr = [int(arr_temp) for arr_temp in input().strip().split()]
# l = set(arr)
# print(len(l))

# Sample Input
#
# 9
# 2 18 24 3 5 7 9 6 12
#
# Sample Output
#
# 24 18 2 3 5 7 9 12 6


n = int(input())
arr = [int(arr_temp) for arr_temp in input().strip().split()]
a = [i for i in arr if i%2]
print(a)