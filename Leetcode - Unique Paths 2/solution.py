class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.uniquePaths(len(obstacleGrid),len(obstacleGrid[0]),0,0,obstacleGrid,{})
    #Recursive solution(With memoization)
    def uniquePaths(self,m,n,i,j,obstacleGrid,memo):
        if i==m or j==n:
            return 0
        if obstacleGrid[i][j]==1:
            return 0
        if i==m-1 and j==n-1:
            return 1
        if (i,j) in memo:
            return memo[(i,j)]
        else:
            memo[(i,j)] = self.uniquePaths(m,n,i+1,j,obstacleGrid,memo)+self.uniquePaths(m,n,i,j+1,obstacleGrid,memo)
            return memo[(i,j)]