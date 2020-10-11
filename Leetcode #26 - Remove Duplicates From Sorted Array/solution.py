class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        used=set()
        fillpos=0
        for v in nums:
            if v not in used:
                nums[fillpos]=v
                used.add(v)
                fillpos+=1
        #nums=nums[:fillpos]
        #print(nums)
        return fillpos