def longest_common_substring(str1, str2):
    cols = len(str1) + 1     # Add 1 to represent 0 valued col for DP
    rows = len(str2) + 1     # Add 1 to represent 0 valued row for DP

    # T = [[0 for _ in range(cols)] for _ in range(rows)]
    T = [[0 for _ in range(cols)] for _ in range(rows)]
    # T = [[0 for j in range(cols)] for i in range(rows)]

    max_length = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if str2[i - 1] == str1[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
                max_length = max(max_length, T[i][j])

    print(T)
    return max_length

if __name__ == '__main__':
    str1 = "abcd"
    str2 = "bc"
    print(longest_common_substring(str1, str2))