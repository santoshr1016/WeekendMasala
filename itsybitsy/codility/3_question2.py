def func1(a_array, b_array):
    size_1 = len(a_array)
    size_2 = len(b_array)
    i, j = 0, 0
    res = []
    while i < size_1 and j < size_2:
        res.append(a_array[i])
        i+=1
        res.append(a_array[i])
        i+=1
        res.append(b_array[j])
        j+=1
    res = res + a_array[i:] + b_array[j:]
    print(res)


def func2(b_array, a_array):
    size_1 = len(a_array)
    size_2 = len(b_array)
    i, j = 0, 0
    res = []
    while i < size_1 and j < size_2:
        for ii in range(2):
            if b_array[i] is not None:
                res.append(b_array[i])
                i+=1
        for jj in range(1):
            if a_array[j] is not None:
                res.append(a_array[j])
                j+=1
    res = res + b_array[i:]
    print(res)


def solution(A, B):
    a_array = ['a']* A
    b_array = ['b']* B

    size_1 = len(a_array)
    size_2 = len(b_array)

    func = func1(a_array, b_array) if size_1 > size_2 else func2(b_array, a_array)

    print(func())



A = 1
B = 4
print(solution(A, B))