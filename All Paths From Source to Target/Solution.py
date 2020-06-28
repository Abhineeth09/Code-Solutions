class Node(object):
    def __init__(self,name):
        self.name=name
        self.list=[]
        self.visited=False
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nodeList=[]
        for i in range(len(graph)):
            n=Node(i)
            n.list=graph[i]
            nodeList.append(n)
        paths=[]
        visited=set()
        def dfs(node,path):
            if node:
                if node.name==len(graph)-1:
                    #print("Found")
                    paths.append(path)
                for n in node.list:
                    dfs(nodeList[n],path+[n])
                    visited.add(n)
        dfs(nodeList[0],[0])
        return paths