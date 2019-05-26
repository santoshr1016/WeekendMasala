def solution(dup_list):
    dup_list.sort()
    left = dup_list[0]
    res = [left]
    size = len(dup_list)
    for i in range(1, size):
        item = dup_list[i]
        if left != item:
            res.append(item)
        left = item

    return res

d_list = [1, 2, 1, 3, 1, 3, 1]
print(solution(d_list))
