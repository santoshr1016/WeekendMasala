def share_market(price):
    size = len(price)
    min_uptil = [0]*size
    max_profit = [0]*size
    highest_profit = float('-inf')

    min_uptil[0] = price[0]
    for i in range(1, size):
        min_uptil[i] = min(min_uptil[i-1], price[i])

    for i in range(size):
        max_profit[i] = price[i] - min_uptil[i]

        highest_profit = max(highest_profit, max_profit[i])
        # if highest_profit < max_profit[i]:
        #     highest_profit = max_profit[i]

    return highest_profit


p = [8, 1, 2, 4, 6, 3]
print(share_market(p))
