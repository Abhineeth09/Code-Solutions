class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftidx,rightidx=-1,-1
        #Finding the First Position using Binary Search
        #Keep finding target using Bsearch and store the index
        # Every time the target is found, search for target towards the left
        # to find First Index
        # Similarly, every time the target is found, search for target on the right
        # to find Last Index
        
        ##Finding First Index
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                #print('Found at',m)
                r=m-1
                leftidx=m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        ##Finding Last Index
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                print('Found at',m)
                l=m+1
                rightidx=m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        #print(leftidx,rightidx)
        return [leftidx,rightidx]