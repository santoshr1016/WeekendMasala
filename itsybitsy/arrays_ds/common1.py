from collections import OrderedDict


def first_non_repeating_char(s="geekforgeeks"):
    print([item for item in s if s.count(item) == 1][0])
    # lst = []
    # tmp_dict = OrderedDict()
    # for ch in s:
    #     if ch in tmp_dict:
    #         tmp_dict[ch] = tmp_dict.get(ch) + 1
    #     else:
    #         tmp_dict[ch] = 1
    #         lst.append(ch)
    # for x in lst:
    #     if tmp_dict[x] == 1:
    #         print(x)

first_non_repeating_char()


def palindrome(a_string):

    a_string = a_string.lower()
    start = 0
    end = len(a_string) -1

    while start <= end:
        if a_string[start] == a_string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

test = "Nayan"
print(palindrome(test))


def reverse_the_digits(num):
    ret = 0
    while num:
        digit = num % 10
        num = num // 10
        ret = ret*10 + digit
    return ret

print(reverse_the_digits(54321))


def reverse_the_strings(ss):
    ss = list(ss)
    start = 0
    end = len(ss) - 1
    while start <= end:
        ss[start], ss[end] = ss[end], ss[start]
        start += 1
        end -= 1
    return ''.join(ss)


print(reverse_the_strings("San"))
