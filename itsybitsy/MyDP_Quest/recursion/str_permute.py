def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
        print(out)
    else:
        for i, let in enumerate(s):
            ss = s[:i] + s[i+1:]
            for perm in permute(ss):
                out += [let + perm]
    return out


print(permute("abc"))

