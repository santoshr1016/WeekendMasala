"""
Input : lst = [[1, 3, 5], [1, 3, 5, 7], [1, 3, 5, 7, 9]]
        x = 1
Output : 3
"""
lst = [[1, 3, 5], [1, 3, 5, 7], [1, 3, 5, 7, 9]]
x = 1
count = 0
for item in lst:
    if x in item:
        count += 1
print(count)

print(sum([1 for item in lst if x in item]))
print(sum(x in item for item in lst))

"""
## Sort list by size of list
ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8], 
                [1, 2, 3, 4, 5], [2]] 
"""

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5], [2]]
ini_list.sort(key = len)
print(ini_list)

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5], [2]]
ini_list.sort(key=lambda x: len(x))
print(ini_list)

"""
op = [['of'], ['The', 'art'], ['programming']]
"""
the_list = ['The', 'art', 'of', 'programming']
the_list.sort(key=len)
print(the_list)
ll = [list(item) for item in the_list]
print(ll)