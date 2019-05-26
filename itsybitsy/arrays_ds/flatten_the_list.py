# 1 Method
the_list = [[1,2],[3,4],[5,6]]
flatten_list = sum(the_list, [])
print(flatten_list)

# 2nd Method
from functools import reduce

list_of_lists = [[1,2],[3,4],[5,6]]
print(reduce(lambda x,y: x+y,list_of_lists))

# 3rd Method
list_of_lists = [[1,2],[3,4],[5,6],[7,8]]
flatten = [item for sublist in list_of_lists for item in sublist]
print(flatten)

# res = []
# for sublist in list_of_lists:
#     for item in sublist:
#         res.append(item)


