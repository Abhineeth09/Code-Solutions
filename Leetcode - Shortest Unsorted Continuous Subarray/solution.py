class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        minIndex,maxIndex=0,len(nums)-1
        while minIndex<=maxIndex-1 and nums[minIndex]<=nums[minIndex+1]:
            minIndex+=1
        while maxIndex>0 and nums[maxIndex]>=nums[maxIndex-1]:
            maxIndex-=1
        if minIndex>maxIndex:
            return 0
        tempMin=min(nums[minIndex:maxIndex+1])
        tempMax=max(nums[minIndex:maxIndex+1])
        while minIndex>0 and nums[minIndex-1]>tempMin:
            minIndex-=1
        while maxIndex<len(nums)-1 and nums[maxIndex+1]<tempMax:
            maxIndex+=1
        return maxIndex-minIndex+1