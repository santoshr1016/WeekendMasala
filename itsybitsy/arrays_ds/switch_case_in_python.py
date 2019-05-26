def operate_on(func, x, y):
    if func == 'add':
        return x+y
    elif func == 'mul':
        return x*y
    elif func == 'sub':
        return x-y
    elif func == 'div':
        return x/y
    else:
        return None


def operate_using_dict(func, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y,
    }.get(func, lambda: None)()

print(operate_on('add', 3, 4))
print(operate_using_dict('mul', 3, 4))


