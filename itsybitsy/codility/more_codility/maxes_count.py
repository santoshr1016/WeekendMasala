def solution(nums, maxes):
    nums.extend(maxes)
    nums.sort()
    res = list()
    count = 0
    for item in maxes:
        l = [i for i, e in enumerate(nums) if e == item]
        res.append(l.pop() - count)
        count += 1
    print(res)


def solution_buggy(nums, maxes):
    nums.extend(maxes)
    nums.sort()
    res = list()
    count = 0
    for item in maxes:
        idx = nums.index(item)
        res.append(idx - count)
        count += 1
    print(res)


nums = [1, 2, 3]
maxes = [2, 4]
solution(nums, maxes)

nums = [1, 4, 2, 4]
maxes = [3, 5]
solution(nums, maxes)

l = [1, 2, 3, 3, 3, 4, 5]
for item in l:
    ll = [idx for idx, ele in enumerate(l) if ele == item]
    print(ll.pop())

