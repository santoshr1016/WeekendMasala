def lc_sub_seq(s1, s2, idx1, idx2):
    if idx1 == len(s1) or idx2 == len(s2):  # at End Empty string subseq with anything is 0
        return 0

    # case 1
    if s1[idx1] == s2[idx2]:
        return 1 + lc_sub_seq(s1, s2, idx1+1, idx2+1)

    # case 2
    c1 = lc_sub_seq(s1, s2, idx1+1, idx2)
    c2 = lc_sub_seq(s1, s2, idx1, idx2+1)

    return max(c1, c2)


def lc_sub_seq_dp(s1, s2):
    """
    dp = [[0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]
    max_len = 0

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            # max_len = max(max_len, dp[i][j])
            if dp[i][j] > max_len:
                max_len = dp[i][j]

    return max_len
    """
    m = len(s1)
    n = len(s2)
    matrix = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[m][n]


# s1 = "abdca"
# s2 = "cbda"
# s1 = "passport"
# s2 = "ppsspt"
s1 = "HelloWorldFrom"
s2 = "HeyWorldfrom"
idx1 = 0
idx2 = 0
print(lc_sub_seq(s1, s2, idx1, idx2))
print(lc_sub_seq_dp(s1, s2))



