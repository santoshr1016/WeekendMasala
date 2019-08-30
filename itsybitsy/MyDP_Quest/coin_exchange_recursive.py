"""
               { 1+𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡−1)
𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠 = 𝑚𝑖𝑛  { 1+𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡−5)
              { 1+𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡−10)
              { 1+𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡−25)

"""


def rec_coin_exchange(coin_list,amt):
    minCoins = amt
    if amt in coin_list:
        return 1
    else:
        for i in [c for c in coin_list if c <= amt]:
            numCoins = 1 + rec_coin_exchange(coin_list,amt-i)
        if numCoins < minCoins:
            minCoins = numCoins
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

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]


def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

# print(rec_coin_exchange([1,5,10,25],63))
# print(rec_coin_exchange([1, 5, 10, 25], 46))
# print(rec_coin_exchange([1, 3, 5, 7], 15))
print(rec_coin_exchange([1, 3, 5, 7], 18))
amnt = 18
clist = [1, 3, 5, 7]
print("Combination needed: ", coin_change_no_of_combinations_needed(18, clist))

# amnt = 98
# clist = [1, 5, 10, 21, 25]

coinsUsed = [0] * (amnt + 1)
coinCount = [0] * (amnt + 1)
print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")

printCoins(coinsUsed, amnt)
print("DSDSDSDSDSD")

# print(coinsUsed)




