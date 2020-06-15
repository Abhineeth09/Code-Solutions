class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathss(m,n,0,0,{})
    '''We calculate all ways in which we reach the bottom right cell. We use recursion and evaluate all possible paths taking only right or down from the current position of (i,j).
    We return 1 if we reach the position(We found a unique way), and return 0 if we go out of bounds. We return the sum of each possibility at each return call and we have the answer. The dictionary memo stores data for memoization.'''
    def uniquePathss(self,m,n,i,j,memo):
        if (i,j) in memo:
            return memo[(i,j)]
        if i==m or j==n:
            return 0
        if i==m-1 and j==n-1:
            return 1
        memo[(i,j)]= self.uniquePathss(m,n,i+1,j,memo)+self.uniquePathss(m,n,i,j+1,memo)
        return memo[(i,j)]