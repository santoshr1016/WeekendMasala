def make_pretty(func):
    def inner():
        print("Inside make pretty function, I will beautify you")
        print("*" * 11)
        func()
        print("*" * 11)
    return inner


# @make_pretty
def normal():
    print("I am inside normal function")

normal = make_pretty(normal)
normal()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return (a/b)


print(divide(5, 2))