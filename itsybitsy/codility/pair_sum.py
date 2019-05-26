def solution_brute_force(ll, pair_sum):
    for item in ll:
        for iitem in ll[1:]:
            if item + iitem == pair_sum:
                print(item, iitem)


def solution_using_set(ll, pair_sum):
    seen = set()
    for item in ll:
        target = pair_sum - item
        if target in seen:
            print(item, target)
        else:
            seen.add(item)


def solution_using_sort(ll, pair_sum):
    ll.sort()
    print(ll)
    i = 0
    j = len(ll) - 1
    while i <= j:
        cur_sum = ll[i] + ll[j]
        if cur_sum == pair_sum:
            print(ll[i], ll[j])
            i += 1
            j -= 1
        elif cur_sum < pair_sum:
            i += 1
        elif cur_sum > pair_sum:
            j -= 1


l = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
pair_sum = 7
print(solution_brute_force(l, pair_sum))
print(solution_using_set(l, pair_sum))
print(solution_using_sort(l, pair_sum))

