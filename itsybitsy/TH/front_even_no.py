def pre_process(arr):
    rev_arr = arr[::-1]
    mapping = list()
    count = 0
    for item in rev_arr:
        if not item % 2:
            count += 1
        mapping.append(count)
    return mapping


def front_even_2(arr):
    mapping = pre_process(arr)
    result = mapping[::-1]
    return result


def front_even(arg_list):
    mod_list = [item%2 for item in arg_list]
    return [mod_list[index:].count(0) for index in range(len(mod_list))]

print(front_even_2([2,8,3,14,68,78]))