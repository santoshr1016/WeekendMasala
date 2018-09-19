from emoji import emojize


def jumping(a):
    jump_dict = {}
    count = 1
    end_of_list = len(a) - 1
    start_idx = 0
    while True:
        next_idx = a[start_idx] + start_idx
        if next_idx > end_of_list or next_idx < 0:
            return count
        else:
            if start_idx in jump_dict:
                return -1
            else:
                jump_dict[start_idx] = next_idx
                count += 1
        start_idx = next_idx
# a = [2, 3, -1, 1, 3]
a = [3, -3, -1, -1, 2]
# a = [3, 3, -1, 1, -2]
# a = [1, 1, -1, 1]

print(emojize(":thumbs_up:")*jumping(a))
