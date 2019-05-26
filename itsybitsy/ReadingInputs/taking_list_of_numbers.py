input()
numbers = list(map(int, input().strip().split(" ")))
print(numbers)

# Approach 2
# Solution 1
N = int(input().strip())
l = [int(i) for i in input().strip().split(" ")]
unique = set(l)
l = list(unique)
l.sort(reverse=True)
print(l[1])

# Solution 2
n = input()
a = map(int, input().split())
a = list(set(a))
a.remove(max(a))
print(max(a))

# Random
N = int(input())
l = input().split()
for i in range(N):
    l[i] = int(l[i])
