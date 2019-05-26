class A(object):
    x = 1
    print("Inside A")


class B(A):
    # print("Inside B")
    pass


class C(B):
    x = 3
    print("Inside C")


class D(B, C):
    print("Inside D")


d = D()
