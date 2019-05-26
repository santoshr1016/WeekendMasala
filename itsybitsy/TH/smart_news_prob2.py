def solution(A):
    # write your code in Python 3.6
    tmp_list = []
    count = 2
    for item in A:
        if item not in tmp_list:
            tmp_list.append(item)
        if len(tmp_list) == 2:
            if item in tmp_list:
                count += 1
            else:
                tmp_list.pop(0)
                count = 2
    return count - 1

A = [5, 4, 4, 5, 0, 12]
print(solution(A))
