
def solution(a_list, size):
    original_set = set(range(1, size+1))
    given_set = set(a_list)
    diff = original_set.difference(given_set)
    return diff.pop()


def solution_2(a_list, size):
    original_set = list(range(1, size+2))
    result = 0
    for item in a_list + original_set:
        result ^= item
    return result


def solution_3(a_list, size):
    tmp_arr = [False]*(size+1)
    for item in a_list:
        tmp_arr[item - 1] = True
    for idx, item in enumerate(tmp_arr):
        if not item:
            return idx + 1

a_list = [1, 2, 3, 4, 6, 10, 9, 8, 5]
print(solution(a_list, 9))
print(solution_2(a_list, 9))
print(solution_3(a_list, 9))

