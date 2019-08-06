for i in range(5):
    print(str.center("#"*(2*i+1), 40))
# for i in range(4, -1, -1):
#     print(str.center("#"*(2*i+1), 20))

"""
count max 1s in Binary String
"""
bin_string = '11000111101010111'
op = max(map(len, bin_string.split('0')))
print(op)