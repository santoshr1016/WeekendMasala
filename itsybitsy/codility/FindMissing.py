
def solution(a_list, size):
    original_set = set(range(1, size+1))
    given_set = set(a_list)
    diff = original_set.difference(given_set)
    return diff.pop()


a_list = [1, 2, 3, 4, 6, 7, 9, 8, 10]
print(solution(a_list, 10))

