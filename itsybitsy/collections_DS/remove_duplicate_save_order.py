def ordered_remove_duplicate(ll):
    seen = set()
    for item in ll:
        if item not in seen:
            yield item
            seen.add(item)


# Problem with this is Since hashes the item, the order is not maintained
def normal_remove_duplicate(ll):
    seen = set()
    for item in ll:
        if item not in seen:
            seen.add(item)
    return seen

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(normal_remove_duplicate(a))
print(list(ordered_remove_duplicate(a)))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(a)
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
