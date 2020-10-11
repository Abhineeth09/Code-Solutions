class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxdist=nums[0]
        #Keep track of the maximum distance you can reach, if you come to an index you cant reach, return false
        for i,v in enumerate(nums):
            if maxdist<i:
                return False
            if maxdist>=len(nums):
                return True
            maxdist=max(maxdist,i+nums[i])
        return True