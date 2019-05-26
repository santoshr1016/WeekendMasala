the_list = [1,2,3,4, "key", "value", "k2", "val2"]
the_zip = zip(the_list[0::2], the_list[1::2])
print(the_list[0::2])
print(the_list[1::2])
another_list = list(zip(the_list[0::2], the_list[1::2]))
print(another_list)
for item in the_zip:
    print(item)
the_dict = dict(zip(the_list[0::2], the_list[1::2]))
print(the_dict)

#########
#program to count the elements in the list
sample_list = [1,2,3,4,1,2,33,55,6,7,88,6,1,1,1,2]
count_of_1 = sample_list.count(1)
print(count_of_1)
l = [[x,sample_list.count(x)] for x in set(sample_list)]
print(l)

x = [1,2,3,4,1,2,33,55,6,7,88,6,1,1,1,2]
y = zip(*[iter(x)]*3)
print(list(y))

