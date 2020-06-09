class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #Two methods - Recursive and iterative
    ## Recursive Approach
    #    Check if the last element of strings is equal
    #    If yes, increase the counter, then remove the last element and compare the remaining strings
    #    If not, then take the max of (s1[include last element],s2[exclude last element],
    #        (s1[exclude last element],s2[include last element]))
    ## Memorization - Use a dictionary to avoid calculating same recursive function again    
    ##Code1 
     
        memory=dict()    
        def recursiveLcs(s1,s2):
            #Edge case
            #print(s1,s2)
            if len(s1)==0 or len(s2)==0:
                return 0
            elif (s1,s2) in memory:
                return memory[s1,s2]
            elif s1[-1]==s2[-1]:
                state=(s1,s2)
                s1=s1[:-1]
                s2=s2[:-1]
                memory[state]=recursiveLcs(s1,s2)+1
                return memory[state]
            else:
                return max(recursiveLcs(s1[:-1],s2),recursiveLcs(s1,s2[:-1]))
        # 2. Iterative approach
        # We make a 2D array(table) and each entry corresponds to the largest subsequence length found at the           index
        # Example
        # s1=abe s2=abcde answer=abe
        #     0 a b c d e
        #   0 0 0 0 0 0 0
        #   a 0 1 1 1 1 1
        #   b 0 1 2 2 2 2
        #   e 0 1 2 2 2 3-> Max Length
        def iterativeLcs(s1,s2):
            m = len(s1)
            n = len(s2)
            dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
            for row in range(1, m + 1):
                for col in range(1, n + 1):
                    if s1[row - 1] == s2[col - 1]:
                        dp[row][col] = 1 + dp[row - 1][col - 1]
                    else:
                        dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
    
            return memo[m][n]
        return iterativeLcs(text1,text2) 