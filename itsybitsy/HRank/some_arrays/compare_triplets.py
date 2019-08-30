alice = [int(item) for item in input().strip().split()]
bob = [int(item) for item in input().strip().split()]
criteria = 3
res = [0,0]
for i in range(criteria):
    if alice[i] > bob[i]:
        res[0] = res[0] + 1
    elif alice[i] < bob[i]:
        res[1] = res[1] + 1
    else:
        pass
print(res)
# print([item for item in res if item > 0])


