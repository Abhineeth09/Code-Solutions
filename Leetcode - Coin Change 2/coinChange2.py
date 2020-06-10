class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0 for _ in range((amount+1))] for _ in range(len(coins)+1)]
        #DP Solution
        #Each row corresponds to the number of coins taken
        #Each column is an integer amount value
        #Each dp[i][j] is the number of ways to make amount j from coins i
        #Fill first column with 1 since there is 1 way to make amount 0 - take no coins
        for i in dp:
            i[0]=1
        #For each increasing row, you have 2 options, take the coin and dont take the coin
        #Take the sum of both options and thats the answer for each dp[i][j]
        #if amount is lesser than coin, just take the value without coins i.e.dp[i-1][j]
        #otherwise take the sum = dp[i-1][j] + dp[i][j-coins[i]]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i!=0 and j!=0:
                    #print(i,j)
                    if coins[i-1]>j:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        return dp[-1][-1]                
        #for i in dp:
            #print(i)