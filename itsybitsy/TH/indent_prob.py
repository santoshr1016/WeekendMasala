FILENAME = "indent_prob.txt"


def make_indents(special_chars):
    print(special_chars)
    list_of_star = []
    result = []
    len_spec_chars = len(special_chars) - 1
    i = 0
    while i < len_spec_chars:
        ch = special_chars[i]
        if ch == "*":
            list_of_star.append(ch)
            result.append(len(list_of_star))
        if ch == "." and special_chars[i+1] == "..":
            print("+")
        if ch == ".." and special_chars[i + 1] == "...":
            print("san")
        i += 1
    print(result)


def indent_prob():
    special_chars = []
    with open(FILENAME) as file:
        for line in file:
            if len(line.strip()) > 0:
                special_chars.append(line.split()[0])
    make_indents(special_chars)
indent_prob()