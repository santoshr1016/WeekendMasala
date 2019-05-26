def rev_sentence(s):
    words = []
    size = len(s)
    i = 0

    while i < size:
        if s[i] is not " ":
            start = i
            while i < size and s[i] is not " ":
                i += 1
        words.append(s[start:i])
        i += 1
    return ' '.join(reversed(words))


def rev_sentence2(s):
    words = s.strip().split()
    return ' '.join(reversed(words))

print(rev_sentence2("This is the work"))
print(rev_sentence("This is the work hello"))
