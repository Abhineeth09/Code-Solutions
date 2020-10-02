class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Getting all combinations and evaluating them
        results = []
        target_length = 2
        used={}
        for i in candidates:
            if i in used:
                used[i]+=1
            else:
                used[i]=1
        print(used)
        def combination(startpos,path,candidates,used):
            if sum(path)==target:
                results.append(path)
                return
            if sum(path)>target:
                return
            zeros=[]
            for k,v in used.items():
                if v==0:
                    zeros.append(k)
            tcand=list(set(candidates).difference(set(zeros)))
            for i in range(startpos,len(tcand)):
                if used[tcand[i]]>0:
                    tempUsed=used.copy()
                    tempUsed[tcand[i]]-=1
                    tempPath=path+[tcand[i]]
                    tempCand=tcand.copy()
                    tempCand=tempCand.remove(tcand[i])
                    #if tempCand:
                    #    combination(i,tempPath, tempCand)
                    combination(i,tempPath,tcand,tempUsed)
                    #candidates.remove(candidates[i])
                    #used.add(candidates[i])
        combination(0,[],candidates,used)
        return results