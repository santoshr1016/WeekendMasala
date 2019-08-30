# N = int(input());
# M = int(input());
#
# data = []
#
# for i in range(0, N):
#     data.append([int(j) for j in input().split()])
#
# res = []
# for d in data:
#     if (d[1] // M) > M:
#         res.append(d[0])
#
# if len(res) == 0:
#     return 0
# else:

from collections import Counter
n,k = input().split()
s = input()
count = Counter(s)
top = count.most_common(1)
print(top[1])
s = sorted(count.items(), key=lambda i: i[1])
print(s)
first = s[0]
second = s[1]
val = max(first[1], second[1])
print()





