# Approach 1
testStr = input()
testStr = [s.upper() if s.islower() else s.lower() for s in testStr]
test = ''.join(testStr)
print(test)

# Approach 2
name = input()
print(''.join(c.lower() if c.isupper() else c.upper() for c in name))

