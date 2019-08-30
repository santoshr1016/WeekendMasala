def domino_arrangements(n):
    ways = [None]*n

    ways[0] = 1
    ways[1] = 1

    for i in range(2, n):
        ways[i] = ways[i-1] + ways[i-2]
    print(ways)
    return ways[i]

n = 15
print(domino_arrangements(n))
