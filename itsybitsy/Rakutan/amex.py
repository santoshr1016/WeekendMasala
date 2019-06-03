def solution(pwd):
    pwd.lower()
    words = pwd.split(' ')
    res = []
    for word in words:
        alpha_numeric = 0
        digits = 0
        for ch in word:
            if ch.isalpha():
                alpha_numeric += 1
            if ch.isdigit():
                digits += 1
            if ch in "[@_!#$%^&*()<>?/\|}{~:]":
                break
        if digits % 2 and not alpha_numeric % 2:
            alpha_numeric += digits
            res.append(alpha_numeric)

    if len(res) == 0:
        return -1

    res.sort()
    return res.pop()

s = "test 5 a0A pass007 ?xy1"
print(solution(s))
