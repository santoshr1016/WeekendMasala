def rec_coin_exchange(coin_list,amt):
    minCoins = amt # Some random number
    if amt in coin_list:
        return 1
    else:
        # This is actually doing DFS, DFS'ing each path of the tree
        # Top Down Approach
        for i in [c for c in coin_list if c <= amt]:
            numCoins = 1 + rec_coin_exchange(coin_list, amt-i)

        minCoins = min(minCoins, numCoins)

    return minCoins


def coin_change_no_of_combinations_needed(n, coins):
    arr = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]

    if n == 0:
        return 0
    else:
        return arr[n]


def dp_bottom_up(coin_list, amt):
    dp = [amt+1]*(amt+1)
    dp[0] = 0
    for i in range(1, amt+1):
        for coin_idx in range(len(coin_list)):
            if coin_list[coin_idx] <= i:
                dp[i] = min(dp[i], dp[i-coin_list[coin_idx]]) + 1
    return dp[amt]


# print(rec_coin_exchange([1,5,10,25], 26))
# print(rec_coin_exchange([1, 5, 10, 25], 63)) # Takes hell lots of time
print("Combination needed: ", coin_change_no_of_combinations_needed(63, [1, 5, 10, 25]))

print(dp_bottom_up([1, 5, 10, 25], 63))
print(dp_bottom_up([1, 5, 10, 25], 11))
print(dp_bottom_up([1, 5, 10, 25], 26))

