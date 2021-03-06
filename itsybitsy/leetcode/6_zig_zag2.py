def convert(s, numRows):
    res = [""] * numRows
    rows = numRows - 1
    going_down = True
    count = 0
    for letter in s:
        if going_down:
            res[count] = res[count] + letter
            count += 1
        if not going_down:
            count -= 1
            res[count] = res[count] + letter
        if count <= 0:
            going_down = True
            count += 1
        if count > rows:
            going_down = False
            count -= 1

    return "".join(res)


s = "PAYPALISHIRING"
numRows = 4

print(convert(s, numRows))
