# Approach 1

N = int(input().strip())
l = list()
for i in range(N):
    l.append([input(), float(input())])

# Approach 2
inp = [[input(), float(input())] for i in range(input())]

# Approach 3

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika o/p

data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
marks = data[input()]
print("%.2f" % (sum(marks)/len(marks)))





