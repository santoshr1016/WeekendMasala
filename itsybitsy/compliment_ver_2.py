def pre_process(arr):
    freq_dict = dict()

    for item in arr:
        count = freq_dict.get(item, 0)
        count += 1
        freq_dict[item] = count

    return freq_dict


def solution(num, arr):
    freq_dict = pre_process(arr)
    count = 0
    for key in arr:
        if num - key in freq_dict:
            count += freq_dict.get(num-key)
    return count


arr = [1, 8, -3, 0, 1, 3, -2, 4, 5]
print(solution(6, arr))




