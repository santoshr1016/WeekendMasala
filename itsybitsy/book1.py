from operator import itemgetter


def top_bookings():
    l = []
    for i in range(int(input())):
        l.append(tuple(map(int, input().strip().split(' '))))
    l.sort(key=lambda elem: elem[1])
    s = set()
    f = []
    for item in l:
        if item[0] in s:
            pass
        else:
            s.add(item[0])
            f.append(item)
    f = f[::-1]
    for i in f:
        print(i[0])

top_bookings()

'''

4
1000 8
2000 8
2000 10
1000 9

'''