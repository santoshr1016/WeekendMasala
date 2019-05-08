def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # return sorted(s1) == sorted(s2)
    if len(s1) != len(s2):
        return False
    count_dic = {}
    for ch in s1:
        count_dic[ch] = count_dic.get(ch, 0) + 1
    for ch in s2:
        count_dic[ch] = count_dic.get(ch, 0) - 1

    for v in count_dic.values():
        if v:
            return False
    return True

print(anagram(s1="dogs ", s2=" GODS "))