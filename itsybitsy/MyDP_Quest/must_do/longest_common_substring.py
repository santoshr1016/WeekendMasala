def lcs_rec(s1, s2, idx1, idx2, count):
    if idx1 == len(s1) or idx2 == len(s2):
        return count
    if s1[idx1] == s2[idx2]:
        count = lcs_rec(s1, s2, idx1 + 1, idx2 + 1, count + 1)
    c1 = lcs_rec(s1, s2, idx1 + 1, idx2, 0)
    c2 = lcs_rec(s1, s2, idx1, idx2 + 1, 0)

    return max(count, max(c1, c2))


def lcs_dp(s1, s2, dp, idx1, idx2, count):
    if idx1 == len(s1) or idx2 == len(s2):
        return count

    if not dp[idx1][idx2][count]:
        c1 = count
        if s1[idx1] == s2[idx2]:
            c1 = lcs_dp(s1, s2, dp, idx1 + 1, idx2 + 1, count + 1)
        c2 = lcs_dp(s1, s2, dp, idx1 + 1, idx2, 0)
        c3 = lcs_dp(s1, s2, dp, idx1, idx2 + 1, 0)

        dp[idx1][idx2][count] = max(c1, max(c2, c3))

    return dp[idx1][idx2][count]


def lcs_dp2(s1, s2):
    dp = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
    max_len = 0
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if max_len < dp[i][j]:
                    max_len = dp[i][j]
    return max_len

# [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
# s1 = "abdca"
# s2 = "cbda"
# s1 = "passport"
# s2 = "ppsspt"
s1 = "HelloWorldFrom"
s2 = "HeyWorldfrom"
idx1 = 0
idx2 = 0
count = 0
max_len = max(len(s1), len(s2))
dp = [[[None for _ in range(len(s1))] for _ in range(len(s2))] for _ in range(max_len)]

print(lcs_rec(s1, s2, idx1, idx2, count))
print(lcs_dp(s1, s2, dp, idx1, idx2, count))
# for item in dp:
#     for it in item:
#         print(it)
#     print()
print(lcs_dp2(s1, s2))
