class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #Getting all combinations and evaluating them
        results = []
        target_length = 2
        def combination(startpos,path):
            if sum(path)==target:
                results.append(path)
                return
            if sum(path)>target:
                return
            for i in range(startpos,len(candidates)):
                tempPath=path+[candidates[i]]
                combination(i,tempPath)
        combination(0,[])
        return results