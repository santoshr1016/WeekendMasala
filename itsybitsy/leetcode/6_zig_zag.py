def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        going_down = True
        j = 0
        rows = []
        row = 0
        numRows1 = numRows - 1

        for letter in s:
            if row >= len(rows):
                rows.append(letter)
            else:
                rows[row] += letter
            j += 1  # number of letters added so far on the latest up or down leg
            row = row + 1 if going_down else row - 1  # increase or decrease row for the next letter
            if j == numRows1:  # reset going_down for next loop
                going_down = not going_down
                j = 0
        return ''.join(rows)


s = "PAYPALISHIRING"
numRows = 4

print(convert(s, numRows))
