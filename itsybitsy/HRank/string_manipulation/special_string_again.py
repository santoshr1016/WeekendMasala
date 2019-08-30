"""
1
11 11 11 11 5 5 6 6 8 8 8 8 2 2 2 2
8
5 4 5 4 5 4 5 4 5 3 2 1 2 3 4 1 2 3 4 5 3 3 4 3 2 2 2 1 1 1 4 4 4 4 4 5 5 5 5 5 5 3 3 3 3 3

"""


def migratory_bird2():
    n = int(input())

    list_of_birds = [int(item) for item in input().strip().split()]

    # list_of_birds = [1, 1, 1, 1, 5, 5, 2, 2, 4, 4, 4, 4, 3, 3, 3, 3]

    size = len(list_of_birds)
    tmp_ans = [0]*6

    for item in list_of_birds:
        tmp_ans[item] += 1

    max_item = tmp_ans[0]

    for item in range(1, size):
        max_item = max(list_of_birds[item], max_item)
    print("ID is:", tmp_ans.index(max(tmp_ans)))
    print(tmp_ans)

# def migratory_bird():
#     n = int(input())
#
#     list_of_birds = [int(bird) for bird in input().strip().split()]
#     tmp_dict = dict()
#     tmp_list = list()
#     for item in list_of_birds:
#         if item not in tmp_dict:
#             tmp_dict[item] = 1
#             tmp_list.append(item)
#         else:
#             tmp_dict[item] = tmp_dict[item] + 1
#     max_val = 0
#     for val in tmp_dict.values():
#         max_val = max(val, max_val)
#
#     for key in sorted(tmp_dict.keys()):
#         if tmp_dict[key] == max_val:
#             print("Lowest ID key:", key)
#             break


migratory_bird2()