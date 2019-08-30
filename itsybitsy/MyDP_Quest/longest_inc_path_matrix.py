# rows = 4
# cols = 3
#
# # matrix = [[int(input()) for j in range(cols)] for i in range(rows)]
# matrix = [[0 for j in range(cols)] for i in range(rows)]
# # matrix = [[0]*cols for i in range(rows)]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()


def longestIncreasingPath(matrix):
    def dfs(i,j,prev):
        if i<0 or j<0 or i>=rows or j>=cols or matrix[i][j]<=prev:
            return 0
        if dp[i][j] != None:
            return dp[i][j]
        v=matrix[i][j]

        right = dfs(i,j+1,v)
        left = dfs(i,j-1,v)
        down = dfs(i+1,j,v)
        up = dfs(i-1,j,v)

        dp[i][j]=max(right, left, down, up) + 1
        return dp[i][j]
    res=0
    rows=len(matrix)
    cols=len(matrix[0]) if rows else 0
    dp=[[None]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            res=max(res,dfs(i,j,float('-inf')))
    return res


matrix = [[9,9,4], [6,6,8], [2,1,1]]
print(longestIncreasingPath(matrix))
