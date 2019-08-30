def in_place(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    print(lst)


def palindrome(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        if lst[start] == lst[end]:
            start += 1
            end -= 1
        else:
            return False
        if start >= end:
            break
    return True

lst = [11, 22, 33, 44, 55, 66, 77]
in_place(lst)


def rev_int(n=4321):
    num = 0
    while n>0:
        num = num*10 + n%10
        n = n//10

    print(num)


str1 = "anana"
print(palindrome(str1))
rev_int()
