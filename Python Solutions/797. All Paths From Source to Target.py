# LeetCode Problem Title : 797. All Paths From Source to Target
# LeetCode Problem Link  : https://leetcode.com/problems/all-paths-from-source-to-target/
# Solution Explanation   : https://youtu.be/AFKXmplbjg8

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def gotTillEnd(curNode, pathTillCurNode):
            if curNode == (n-1):
                paths.append(pathTillCurNode.copy())
                return
            for nextNode in graph[curNode]:
                gotTillEnd(nextNode, pathTillCurNode + [nextNode])

        n = len(graph)
        paths = []
        gotTillEnd(0, [0])
        return paths
