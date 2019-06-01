def solution(ss, cc):
    print(ss.index(cc))


def solution_2(ss, cc):
    for idx, ch in enumerate(ss):
        if ch == cc:
            print(idx)
            break

solution("hi, this is bitgo test", 't')
solution_2("hi, this is bitgo test", 't')