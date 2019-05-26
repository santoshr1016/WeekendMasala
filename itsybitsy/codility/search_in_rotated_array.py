def binary_search(the_list, key):
    left = 0
    right = len(the_list) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if the_list[mid] == key:
            return mid
        if the_list[mid] >= the_list[left]:
            if the_list[left] <= key < the_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if the_list[mid] < key <= the_list[right]:
                left = mid + 1
            else:
                right = mid - 1

    return found

l = [11, 22, 33, 44, 55, 1, 3, 5, 7, 9]
print(binary_search(l, 44))