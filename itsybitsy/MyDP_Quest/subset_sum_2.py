from itertools import combinations

# lst = [2, 3, 5, 6, 8, 10]
lst = ['a', 'b', 'c']
target = 10
size = len(lst)
for i in range(1, size):
    for c in combinations(lst, i):
        print("".join(list(c)))
        # if sum(c) == target:
        #     print(list(c))


# str1 = "abfdjhsicdefdjhsifslerdfdjhsid"
# str2 = "fdjhsi"
#
# for i in range(len(str1)):
#     if str1.startswith(str2, i):
#         print("Substring Found at {0}".format(i))
# if str1.find(str2):
#     print("found")

# s = input()
