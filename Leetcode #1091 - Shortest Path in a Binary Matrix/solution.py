'''class Graph:
    def __init__(self):
        self.adjacencyDict={}
    #def addNode(node):
    #    self.adjacencyDict[node]=[]
    def addEdge(self,s,v):
        if s not in self.adjacencyDict:
            self.adjacencyDict[s]=[v]
        else:
            self.adjacencyDict[s].append(v)
        if v not in self.adjacencyDict:
            self.adjacencyDict[v]=[s]
        else:
            self.adjacencyDict[v].append(s)'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #g=Graph()
        dist=float('+inf')
        level=0
        q=[]
        visited=set()
        q.append([[0,0],level])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        if len(grid)==1 and grid[0][0]==0:
            return 1
        l=[level]
        #Do a BFS to find the shortest path
        #Dp solution not applicable since we can go in all directions
        while q:
            tempt,level=q.pop(0)
            trow,tcol=tempt
            if grid[trow][tcol]==1:
                return -1
            if trow==len(grid)-1 and tcol==len(grid[0])-1:
                return level+1
            istart,jstart,iend,jend=-1,-1,2,2
            if trow==0:
                istart=0
            elif trow==len(grid)-1:
                iend=1
            if tcol==0:
                jstart=0
            elif tcol==len(grid[0])-1:
                jend=1
            apps=[]
            #Check all connected nodes and push in the queue
            for i in range(istart,iend):
                for j in range(jstart,jend):
                    if grid[trow+i][tcol+j]==0 and str(trow+i)+str(tcol+j) not in visited:
                        q.append([[trow+i,tcol+j],level+1])
                        visited.add(str(trow+i)+str(tcol+j))
        return -1