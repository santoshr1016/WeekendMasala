func = lambda x: x*x

l = [func(i) for i in range(10)]
print(l)

ll = [(lambda x: x*x)(x) for x in range(10)]
print(ll)

