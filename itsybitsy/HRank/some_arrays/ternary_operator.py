"""
Using the ternary operator in Python

"""
a, b = 10, 20

min_num = a if a < b else b
print(min_num)

"""
nested if else 
"""
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")