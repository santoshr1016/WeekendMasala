def rod_cutter_dp(cost, n):
    rod = [0]*(n+1)
    rod[0] = 0
    for i in range(1, n+1):
        max_val = float('-inf')
        for j in range(1, i+1):
            max_val = max(max_val, cost[j]+rod[i-j])
        rod[i] = max_val

    return rod[n]

# cost = [0, 2, 4, 5, 7, 11, 13, 17]
# rod_len = 7
#
cost = [0, 2, 4, 7, 8]
rod_len = 4
print(rod_cutter_dp(cost, rod_len))
