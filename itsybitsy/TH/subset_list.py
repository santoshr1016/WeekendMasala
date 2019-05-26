def sum_pair(arr, n):
    seen = set()
    out = set()

    for item in arr:
        target = n - item
        if target not in seen:
            seen.add(item)
        else:
            # out.add((min(item, target), max(item, target)))
            out.add((item, n - item))
    return out if out else ""


def subset_sum_elegant(numbers, target):
    size = len(numbers)
    for i in range(size):
        diff = target - numbers[i]
        l = sum_pair(numbers[i+1:], diff)
        ll = sum_pair(numbers[:i], diff)
        print(numbers[i], l, ll)


def subset_sum(numbers, target, partial=[]):
    # print(partial)
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    subset_sum([3,9,8,4,5,7,10],15)
    subset_sum_elegant([3,9,8,4,5,7,10],15)