def substrings(s):

    # Declare local variable for the length of s.
    l = len(s)

    # Here I chose range over xrange for python version compatibility.
    for end in range(l, 0, -1):
        for i in range(l-end+1):
            yield s[i: i+end]


# Define palindrome.
def palindrome(s):
    return s == s[::-1]


# Main fnunction.
def Question2(a):
    for l in substrings(a):
        # print(l)
        if palindrome(l):
            print(l)

# print(Question2("abaxabaxabb"))
# print(Question2("banana"))
# print(Question2("abcbaba"))
print(Question2("aaaa"))
# print(Question2("lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"))
# print(Question2("babad"))