def solution(ll):
    ll.sort()
    m = range(1, len(ll))

    x = (set(m) - set(l))
    if not x:
        print(ll.pop() + 1)
    else:
        print(min(x))


l = [1,2,3,4,6,7,8,9]
# l = [0, 10, 2, -10, -20]
solution(l)