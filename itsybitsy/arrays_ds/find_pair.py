def bin_search(item, arr):
    if item in arr:
        return True
    return False


def find_pair(k, arr):
    size = len(arr)
    for i in range(size):
        if bin_search(k-arr[i], arr[i+1:]):
            return True
    return False


def find_pair_using_set(k, arr):
    s = set()
    for item in arr:
        if k - item in s:
            return True
        s.add(item)
    return False


def find_pair_using_2_pointers(k, arr):
    i = 0
    j = len(arr) -1
    while i < j:
        if arr[i] == k - arr[j]:
            return True
        if arr[i] > k - arr[j]:
            j -= 1
        else:
            i +=1
    return False

arr = [1,4,5,7,9,11,14]
k = 21
print(find_pair(k, arr))
print(find_pair_using_set(k, arr))
print(find_pair_using_2_pointers(k, arr))


