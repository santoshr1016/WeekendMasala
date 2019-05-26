a_list = [1,2,3,4,5,6,17,18,19]


def fib(N=10):
    f, s = 0, 1
    for i in range(2, N):
        tmp = f + s
        f = s
        s = tmp
        print(tmp)


def add_new(N=10):
    idx = 0
    for i, j in enumerate(a_list):
        if N < j:
            idx = i
            break
    a_list.insert(idx, N)
    print(a_list)

add_new()
fib()