result = dict()
with open("host_logs.txt") as fd:
    for line in fd:
        hn = line.strip().split()[0]
        result[hn] = result.get(hn, 0) + 1
print(result)