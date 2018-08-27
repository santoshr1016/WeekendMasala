def find_lhs(key, a):
    if key in set(a):
        return True
    return False


def find_rhs(key, a):
    if key in set(a):
        return True
    return False


def solution(comp, a):
    count = 0
    for idx, val in enumerate(a):
        lhs = a[:idx]
        rhs = a[idx+1:]
        if find_lhs(comp - val, a[:idx]):
            # print(idx, lhs.index(comp-val))
            count +=1

        if find_rhs(comp - val, a[idx+1:]):
            # print(idx, rhs.index(comp - val) + idx+1)
            count += 1
    print(count)
a = [1, 8, -3, 0, 1, 3, -2, 4, 5]

solution(6, a)