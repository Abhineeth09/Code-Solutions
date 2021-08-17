class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        while low<high:
            m = (low+high)//2
            if arr[m]<arr[m+1]:
                low = m+1
            else:
                high = m

            
        return low