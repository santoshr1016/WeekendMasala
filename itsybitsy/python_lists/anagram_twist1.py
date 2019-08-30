from collections import Counter
def anagram_twist(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    i = 0
    j = 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            count += 1
            i += 1
    count += len(s1) - i + len(s2) - j
    print("No of char to remove to make it anagram: {0}".format(count))


def removeChars(str1, str2):
    # make dictionaries from both strings
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # extract keys from dict1 and dict2
    keys1 = dict1.keys()
    keys2 = dict2.keys()

    # count number of keys in both lists of keys
    count1 = len(keys1)
    count2 = len(keys2)
    print(count1, count2)
    # convert list of keys in set to find common keys
    set1 = set(keys1)
    commonKeys = len(set1.intersection(keys2))

    if (commonKeys == 0):
        return count1 + count2
    else:
        return (max(count1, count2) - commonKeys)

str1 = "banana"
str2 = "anana"
anagram_twist(str1, str2)

str1 = "cddgk"
str2 = "gcd"
anagram_twist(str1, str2)

str1 = "bca"
str2 = "acb"
anagram_twist(str1, str2)

str1 = "banana"
str2 = "anana"
removeChars(str1, str2)
