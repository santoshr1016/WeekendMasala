def balance(arr):
    if len(arr) % 2:
        return False
    open_paren = set("([{")
    bal_paren = set([('(', ')'), ('[', ']'), ('{', '}')])

    the_stack = []

    for item in arr:
        if item in open_paren:
            the_stack.append(item)
        else:
            if len(the_stack) == 0:
                return False
            top_item = the_stack.pop()
            if (top_item, item) not in bal_paren:
                return False

    return len(the_stack) == 0

print(balance('{{}}'))
