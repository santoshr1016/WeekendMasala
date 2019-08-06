"""
Input = [1, 2, 3, 4, 5, 6, 7]
length_to_split = [2, 1, 3, 1]

Output: [[1, 2], [3], [4, 5, 6], [7]]

"""
from itertools import islice


def split_the_list(inp, split_list):
    input_list = iter(inp)
    result = [list(islice(input_list, item)) for item in split_list]
    print(result)


inp_list = [1, 2, 3, 4, 5, 6, 7]
length_to_split = [2, 1, 3, 1]
split_the_list(inp_list, length_to_split)
