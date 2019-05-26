def decorate():
    print(" I am in decorator")


obj = decorate

@decorate
def fun1():
    print("hello World")



