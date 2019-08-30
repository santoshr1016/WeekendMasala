def reverse(str1):
    if len(str1)<=1:
        return str1
    return str1[1:] + str1[0]
print(reverse("Hello"))