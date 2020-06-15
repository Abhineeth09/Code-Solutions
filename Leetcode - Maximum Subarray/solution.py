class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=0
        #For array with only negative elements
        negative=True
        for val in nums:
            currSum+=val
            if currSum>maxSum:
                maxSum=currSum
            if currSum<0:
                currSum=0
            if negative:
                if currSum>0:
                    negative=False
        if negative:
            return max(nums)
        return maxSum