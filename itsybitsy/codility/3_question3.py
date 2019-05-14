
def solution(A, B):
    str_array = (['a']* A + ['b']* B) if A > B else (['b']* B + ['a']* A)
    smaller = A if A < B else B
    res = []

    while str_array:
        count = 0
        while True:
            if str_array and count < 2:
                res.append(str_array.pop(0))
                count +=1
            else:
                if smaller == 0:
                    print(res)
                    return
                else:
                    break
        if str_array:
            res.append(str_array.pop())
            smaller -= 1

A = 4
B = 10
print(solution(A, B))