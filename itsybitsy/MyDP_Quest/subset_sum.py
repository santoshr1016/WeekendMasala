def ArrayAddition(arr):
    # get largest number and remove it from array
    goal = max(arr)
    arr.remove(goal)

    # clever way to get rid of negative values
    # for i in range(0, len(arr)):
    #     if arr[i] < 0:
    #         goal -= arr[i]
    #         arr[i] = 0

    # table to track elements
    table = [[False] * (goal + 1) for r in range(0, len(arr) + 1)]
    print(table)

    # fill first column
    for i in range(0, len(arr) + 1):
        table[i][0] = True

    # dynamic programming solution
    for i in range(1, len(arr) + 1):
        for j in range(1, goal + 1):
            table[i][j] = table[i - 1][j]
            if table[i][j] == False and j >= arr[i - 1]:
                table[i][j] = table[i][j] or table[i - 1][j - arr[i - 1]]

    if table[len(arr)][goal]:
        return "true"
    else:
        return "false"

"""
    # Find out which Numbers should be in the subset
    # give from index 0
    row -= 1
    col -= 1
    sum_subset = []

    # check if the Subset is possible : if not, return None
    if dp_array[row][col] != req_sum:
        return None

    # get the subset
    while col >= 0 and row >= 0 and req_sum > 0:
        # First Row
        if (row == 0):
            sum_subset.append(weight[row])
            break

        # Bottom-Right most ele
        if (dp_array[row][col] != dp_array[row - 1][col]):
            # print(req_sum,' : ',dp_array[row][col],dp_array[row-1][col],' : ',weight[row])
            sum_subset.append(weight[row])
            req_sum -= weight[row]
            col -= weight[row]
            row -= 1
        else:
            row -= 1

    return sum_subset
"""


print(ArrayAddition([1, 2, 6, 4, 7, 12]))