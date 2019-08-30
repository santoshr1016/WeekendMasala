import time


def dp_way(str1, start, end, dp):
    # base cases
    # print("DP Way")
    # print(timeit.timeit())
    if start > end:
        return 0
    if start == end:
        return 1

    #case 1
    if dp[start][end] == 0:
        if str1[start] == str1[end]:
            dp[start][end] = 2 + dp_way(str1, start+1, end-1, dp)

        #case 2
        else:
            left = dp_way(str1, start+1, end, dp)
            right = dp_way(str1, start, end-1, dp)

            dp[start][end] = max(left, right)
    # print(timeit.timeit())
    return dp[start][end]


def longest_palindrome(str1, start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    #case 1
    if str1[start] == str1[end]:
        return 2 + longest_palindrome(str1, start+1, end-1)

    #case 2
    left = longest_palindrome(str1, start+1, end)
    right = longest_palindrome(str1, start, end-1)

    return max(left, right)

str1 = "rtyftkhkkayakiopiouuhgioyoyi"
start = 0
end = len(str1) - 1
print("recursive  Way")
startt = time.time()
print(longest_palindrome(str1, start, end))
done = time.time()
elapsed = done - startt
print(elapsed)
print("*"*22)

size = len(str1)
dp = [[0 for i in range(size)] for i in range(size)]
start = 0
end = len(str1) - 1

print("DP Way")
startt = time.time()
print(dp_way(str1, start, end, dp))
done = time.time()
elapsed = done - startt
print(elapsed)
