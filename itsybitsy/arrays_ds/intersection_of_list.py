list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 3, 5, 7, 9, 11, 33, 44, 55]

# intersection = [list(filter(lambda x: x in list1, sublist)) for sublist in list2]
l = list(filter(lambda x: x in list1, list2))
print(l)