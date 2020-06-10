class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #DP solution
        #create empty matrix
        Matrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)]
        #columns=str1 rows=str2
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if i==0 or j==0:
                    Matrix[i][j]=i+j
                elif word2[i-1]==word1[j-1]:
                    Matrix[i][j]=Matrix[i-1][j-1]
                else:    
                    Matrix[i][j]=1+min(Matrix[i-1][j],Matrix[i][j-1])
        return Matrix[-1][-1]