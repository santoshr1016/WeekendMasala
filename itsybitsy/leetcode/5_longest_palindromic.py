def longest_palin(s):
    start = 0
    end = len(s)-1
    left = []
    right = []
    while start <= end:
        if s[start] == s[end]:
            left.append(s[start])
            right.insert(0, s[end])
            start += 1
            end -= 1
        else:
            start += 1
            end -= 1

    left.extend(right)

    return "".join(left)

print(longest_palin("aba"))