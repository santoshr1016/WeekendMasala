def solution(the_list, shift):
    for i in range(shift):
        the_list.append(the_list.pop(0))
    return the_list


def solution_move_all_by_1(the_list):
    tmp = the_list[0]
    size = len(the_list) - 1
    for i in range(size):
        the_list[i] = the_list[i+1]
    the_list[size] = tmp
    return the_list


def binary_search(the_list, key):
    left = 0
    right = len(the_list) - 1
    found = False
    while left <= right and not found:
        mid = (left + right) // 2
        if the_list[mid] == key:
            found = True
        else:
            if key > the_list[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return found


def binary_search_recursive(the_list, key):
    if len(the_list) == 0:
        return False
    else:
        mid = len(the_list)//2
        if the_list[mid] == key:
            return True
        else:
            if key > the_list[mid]:
                return binary_search_recursive(the_list[mid+1:], key)
            else:
                return binary_search_recursive(the_list[:mid], key)

the_l = [1, 2, 3, 4, 5, 6, 7]
print(solution(the_l, 3))
print(solution_move_all_by_1(the_l))
print("heoo")
the_l = [18, 39, 45, 56, 88, 99, 121, 323]
print(binary_search(the_l, 39))
print(binary_search_recursive(the_l, 323))


