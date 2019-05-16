def to_weird_case(big):
    flag = True
    l = []
    for ch in big:
        if flag:
            l.append(ch.upper())
            flag = False
        else:
            l.append(ch.lower())
            flag = True
    return "".join(l)
print(to_weird_case('Weird string case'))