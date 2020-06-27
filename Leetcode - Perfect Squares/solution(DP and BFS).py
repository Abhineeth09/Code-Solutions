class Solution:
    def numSquares(self, n: int) -> int:
        #DP Solution
        '''
        #Finding the perfect square numbers that are eligible
        self.num=1
        self.square=1
        self.numList=[]
        while self.square<=n:
            self.square=self.num**2
            if self.square<=n:
                self.numList.append(self.square)
            self.num+=1
        #Using a dp solution
        #initializing a dp matrix
        #len(numList) of rows and n+1 columns
        self.dp=[[None for i in range(n+1)] for j in range(len(self.numList)+1)]
        for i in range(len(self.dp)):
            for j in range(len(self.dp[i])):
                if i==0:
                    self.dp[i][j]=float('+inf')
                elif j==0:
                    self.dp[i][j]=0
                else:
                    if j<self.numList[i-1]:
                        self.dp[i][j]=self.dp[i-1][j]
                    else:
                        self.dp[i][j]=min(1+self.dp[i][j-self.numList[i-1]],self.dp[i-1][j])
                #print(dp[i][j],end=' ')
            #print()
        return self.dp[-1][-1]'''
        #BFS Solution
        #Finding the perfect square numbers that are eligible
        # Think of the problem as a graph, and use the recursion tree for reference
        # You start at 0, and try to reach n
        # You keep appending the next recursion to the queue and return the level at which the first solution is found
        # In a graph, BFS is the shortest path hence you return the optimal solution
        # This is faster than DP
        if n < 2:
            return n
        squares = []
        i = 1
        while i * i <= n:
            squares.append( i * i )
            i += 1
        level = 0
        queue = {n}
        while queue:
            level += 1
            temp = set()
            for x in queue:
                for y in squares:
                    if x == y:
                        return level
                    if x < y:
                        break
                    temp.add(x-y)
            queue = temp

        return level