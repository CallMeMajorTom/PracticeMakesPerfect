#Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.
#The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
#Example:
#Input: [[1,2], [3], [3], []]
#Output: [[0,1,3],[0,2,3]]
#Explanation: The graph looks like this:
#0--->1
#|    |
#v    v
#2--->3
#There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

##TIMEOUT 太蠢辽
class Solution(object):

    def findOrigins(self,graph,origins):
        for i in range(len(graph)):
            for j in range(1,len(graph)):
                if j in graph[i]:
                    origins.append([i,j])
        return origins

    def findPaths(self,origins,target):
        lists = []
        for i in origins:
            for j in origins:
                if(i[-1] == j[0]):
                    tmp = sorted(list(set(i+j)))
                    if tmp not in origins:
                        origins.append(sorted(list(set(i+j))))
        lists = [l for l in origins if (l[0] == 0) and (l[-1] == target)]
        return lists

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        origins = []
        origins = self.findOrigins(graph,origins)
        lists = self.findPaths(origins,len(graph) - 1)
        return lists

#神仙思路：
#solve(node)函数表示求node到终点的paths
#递归
class Solution(object):
    def allPathsSourceTarget(self, graph):
        N = len(graph)

        def solve(node):
            if node == N-1: return [[N-1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)
