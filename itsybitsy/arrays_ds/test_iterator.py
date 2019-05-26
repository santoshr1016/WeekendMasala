class PowTwo:
    def __init__(self, maxi=0):
        self.max = maxi

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

iter_obj = PowTwo(8)
for i in iter_obj:
    print(i)

# This is lengthy right, Lets use generator


def power_two(maxi):
    start = 0
    while start < maxi:
        yield 2**start
        start += 1
gen_obj = power_two(6)
for item in gen_obj:
    print(item)