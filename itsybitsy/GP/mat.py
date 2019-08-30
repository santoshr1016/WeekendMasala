# Complete the interpolate function below.
def interpolate(n, quantity, price):
    zip_val = zip(quantity, price)
    d = {item[0]: item[1] for item in zip_val}

    # print(str(d[n]))
    rv = d[n]
    # return "%.2f".format(rv)
    s = "%.2f" % (rv)
    return s

if __name__ == '__main__':

    n = int(input().strip())

    quantity_count = int(input().strip())

    quantity = []

    for _ in range(quantity_count):
        quantity_item = int(input().strip())
        quantity.append(quantity_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = float(input().strip())
        price.append(price_item)

    res = interpolate(n, quantity, price)
    print(res)
