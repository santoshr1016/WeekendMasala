def jumping(a):
    count = 0
    end_of_list = len(a)-1
    start_idx = 0
    prev_idx = 0
    while True:
        next_idx = a[start_idx] + start_idx
        if prev_idx == next_idx and next_idx < end_of_list:
            print("infinite loop")
            return -1
        count += 1
        if next_idx > end_of_list or next_idx < 0:
            break
        prev_idx = start_idx
        start_idx = next_idx
        # print(prev_idx, start_idx)
    return count

# a = [2, 3, -1, 1, 3]
# a = [3, -3, -1, -1, 2]
a = [3, 3, -1, 1, -2]
# a = [1, 1, -1, 1]

print(jumping(a))
