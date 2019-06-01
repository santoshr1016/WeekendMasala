change = {
    .01: 'PENNY',
    .05: 'NICKEL',
    .10: 'DIME',
    .25: 'QUARTER',
    .50: 'HALF DOLLAR',
    1.00: 'ONE',
    2.00: 'TWO',
    5.00: 'FIVE',
    10.00: 'TEN',
    20.00: 'TWENTY',
    50.00: 'FIFTY',
    100.00: 'ONE HUNDRED'
}

denominations = list(change.keys())
denominations.sort(reverse=True)

price_amt, given_amt = tuple(map(float, input().split(';')))


def solution(price, given):
    result = []
    if given < price:
        print("ERROR")
        return
    elif given == price:
        print("ZERO")
        return
    else:
        amt_return = given - price
        for item in denominations:
            while amt_return >= item:
                result.append(item)
                amt_return -= item
            if amt_return == 0:
                break
    print([change[item] for item in result])




solution(price_amt, given_amt)

