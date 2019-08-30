def helper(l, r, s):
    if l>=r:
        return True
    if s[l] != s[r]:
        return False
    else:
        return helper(l+1, r-1, s)


def palindrome(s):
    start = 0
    end = len(s)-1

    if helper(start, end, s):
        return True
    return False

s = "banana"
print(palindrome(s))
