matrix = []


def is_perm_matrix(m):
    if all(sum(row) == 1 for row in m):
        return all(sum(col) == 1 for col in zip(*m))
    return False


def decimal_to_binary(n):
    return bin(n).replace("0b","")

for i in range(int(input())):
    rows = int(input())
    for _ in range(rows):
        bl = [int(i) for i in decimal_to_binary(int(input()))]
        diff = rows - len(bl)
        for i in range(diff):
            bl.insert(0, 0)
        matrix.append(bl)

print(is_perm_matrix(matrix))