def solution(mystr):
    for item in mystr:
        size = len(item) - 1
        start = 0
        count = 1
        while start < size:
            if item[start] == item[start + 1]:
                count += 1
            else:
                if count >= 2:
                    print("{0}{1}".format(item[start], count), end="")
                else:
                    print("{0}".format(item[start]), end="")
                count = 1
            start += 1

        if count >= 2:
            print("{0}{1}".format(item[start], count))
        else:
            print("{0}".format(item[start]))


def solution2(the_list):
    for mystr in the_list:
        alt = []
        alt.append(mystr[0])
        count = 0
        for c in mystr[1:]:
            if alt[-1] != c:
                alt.append(c)
            else:
                count += 1

        print(alt)

mystr = ['AAAA','BBBBB','ABBBABABAB','BABABA','AAABBB', "aacccacaaa"]

print(solution(mystr))
# print(solution2(mystr))
