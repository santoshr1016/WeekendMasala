def uniq_chars(arr):
    return len(set(arr)) == len(arr)


def uniq_chars2(arr):
    the_set = set()
    for item in arr:
        if item in the_set:
            return False
        else:
            the_set.add(item)
    return True

print(uniq_chars("abcdefwa"))
print(uniq_chars2("abcdefwa"))
