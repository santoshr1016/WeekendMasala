def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for k1, k2 in zip(arr1, arr2):
        if k1 - k2:
            return False
    return True

    # arr1 = sorted(arr1)
    # print(arr1)
    # arr2 = sorted(arr2)
    # print(arr2)
    #
    # return arr2 == arr1


arr1 = [1,2,3,4,5,6]
arr2 = [6,4,3,2,1,15]

print(finder(arr1, arr2))