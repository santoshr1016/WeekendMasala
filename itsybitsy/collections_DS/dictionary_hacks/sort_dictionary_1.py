from collections import defaultdict


str1 = "The lines are printed in reverse order and the meaning is still in order"
dd = defaultdict(list)
lst_str = [item for item in str1.split(" ")]
print(lst_str)
for item in lst_str:
    dd[len(item)].append(item)
for k, v in dd.items():
    print(k, v)

#########################
print("Sorting")
#########################
for k, v in sorted(dd.items(), key=lambda item: item[0]):
    print(k, v)

print("Sorting 2")
for k in sorted(dd.keys()):
    print(k, dd[k])

print("Sorting 3")
for k, v in sorted(dd.items(), key=lambda item: (item[0], item[1])):
    print(k, v)
