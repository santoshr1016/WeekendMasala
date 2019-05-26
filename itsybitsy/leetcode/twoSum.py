def twoSum(arr, target):
    ret_list = []
    the_set = set()
    for idx in range(len(arr)):
        if (target - arr[idx]) in the_set:
            return [arr.index(target - arr[idx]), idx]
        else:
            the_set.add(arr[idx])
    return ret_list


arr = [2, 7, 11, 15]
target = 9
print(twoSum(arr, target))
