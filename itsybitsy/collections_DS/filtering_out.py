mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([i for i in mylist if i>0])
print([i for i in mylist if i<0])



# One potential downside of using a list comprehension is that it
# might produce a large result if the original input is large.

# Use generator comprehension

g = (item for item in mylist if item > 0)
for i in g:
    print(i)
for item in (item for item in mylist if item > 0):
    print(item, end=' ')

# Sometimes, the filtering criteria cannot be easily expressed in a
# list comprehension or generator expression

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)


clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

# Why this is important, If you put condition in like in line 4
# the element is skipped, But in this you are putting 0s by putting
# condition in the front

