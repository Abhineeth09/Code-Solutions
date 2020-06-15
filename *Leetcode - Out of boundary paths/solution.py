class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        #recursive solution
        return self.findPathss(m,n,N,i,j,{})%(10**9+7)
    def findPathss(self,m,n,N,i,j,memo):
        #recursion with memoization solution
        if (i,j,N) in memo:
            return memo[(i,j,N)]
        if i==m or j==n or i<0 or j<0:
            return 1
        if N==0:
            return 0
        else:
            memo[(i,j,N)]=(self.findPathss(m,n,N-1,i+1,j,memo)+self.findPathss(m,n,N-1,i,j+1,memo)+self.findPathss(m,n,N-1,i-1,j,memo)+self.findPathss(m,n,N-1,i,j-1,memo))
        return memo[(i,j,N)]