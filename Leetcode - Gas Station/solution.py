class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        counter=0
        net=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(2*len(gas)):
            counter+=1
            n=i%len(gas)
            net+=gas[n]-cost[n]
            if net<0:
                start=n+1
                counter=0
                net=0
            if counter==len(gas):
                return start
            #print('iter',n,'start',start,'count',counter,'net',net)
        return start