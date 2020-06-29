class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #DP Solution
        #Init First row with sum[only way to reach there is in first row], same for first col
        #Then the min sum for each [i,j] is the min from path above it, or from left, take min and add the existing value of [i,j] to get min val to reach there
        #return lastr pos
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j-1] + grid[i][j]   
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        return dp[-1][-1]