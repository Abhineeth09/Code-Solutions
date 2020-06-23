class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        gmax,maxp,minp=nums[0],nums[0],nums[0]
        #Keeping track of the minimum and maximum values
        #Storing global max in gmax
        #Storing min value since -ve * -ve = Positive might occur at any index
        for idx,n in enumerate(nums):
            if idx==0:
                continue
            candidates=(n,n*minp,n*maxp)
            minp=min(candidates)
            maxp=max(candidates)
            gmax=max(gmax,maxp)
        return gmax