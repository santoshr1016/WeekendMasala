def stock_prices2(arr):
    min_stock_price = arr[0]
    max_profit = 0

    for item in arr:
        min_stock_price = min(item, min_stock_price)
        profit_margin = max(max_profit, item - min_stock_price)
        max_profit = max(profit_margin, max_profit)
    print(max_profit)


def stock_prices(arr):
    size = len(arr)
    diff_list = []
    for i in range(size):
        cur_max = 0
        for j in range(i+1, size):
            diff = arr[j] - arr[i]
            if diff > cur_max:
                cur_max = diff
        diff_list.append(cur_max)
    print(diff_list)


stock_prices2([12, 11, 5, 2, 10])




