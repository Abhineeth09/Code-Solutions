class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans=[]
        clash=[]
        for i in intervals:
            #if interval clashes
            if (newInterval[0]<=i[-1] and newInterval[0]>=i[0]) or (newInterval[-1]<=i[-1] and newInterval[-1]>=i[0]) or (i[0]>=newInterval[0] and i[-1]<newInterval[-1]) or (newInterval[0]>=i[0] and newInterval[-1]<i[-1]):
                clash.append(i)
                continue
            else:
                ans.append(i)
        if clash:
            r=[clash[0][0],clash[-1][-1]]
            r=[min(r[0],newInterval[0]),max(r[-1],newInterval[-1])]
        else:
            r=newInterval
        #print(ans,clash,r)
        l=[]
        l.append(ans)
        l=l[0]
        l.append(r)
        #print(l)
        return sorted(l)