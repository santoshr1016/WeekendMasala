def lps_recursive(s, start, end):
    if start > end:
        return 0
    if start == end:  # every sequence with one element is a palindrome of length 1
        return 1

    # case 1: elements at the beginning and the end are the same
    if s[start] == s[end]:
        return 2 + lps_recursive(s, start+1, end-1)

    # case 2: skip one element either from the beginning or the end
    c1 = lps_recursive(s, start + 1, end)
    c2 = lps_recursive(s, start, end-1)

    return max(c1, c2)


def lps_dp(s, dp, start, end):
    result = []
    if start > end:
        return 0
    if start == end:  # every sequence with one element is a palindrome of length 1
        return 1

    if not dp[start][end]:
        # case 1: elements at the beginning and the end are the same
        if s[start] == s[end]:
            dp[start][end] = 2 + lps_dp(s, dp, start+1, end-1)

        # case 2: skip one element either from the beginning or the end
        else:
            c1 = lps_dp(s, dp, start + 1, end)
            c2 = lps_dp(s, dp, start, end-1)

            dp[start][end] = max(c1, c2)

    return dp[start][end]

# str1 = "abdbca"
# str1 = "cddpd"
# str1 = "pqrabc"
# str1 = "aabcdebaz"
# str1 = "abcda"
str1 = "banana"


size = len(str1)
start = 0
end = size - 1
print(lps_recursive(str1, start, end))

# dp = [[None] * size for i in range(size)]
# print(lps_dp(str1, dp, start, end))
# for item in dp:
#     print(item)


