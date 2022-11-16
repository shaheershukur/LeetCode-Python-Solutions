# LeetCode Problem Title : 329. Longest Increasing Path in a Matrix
# LeetCode Problem Link  : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Solution Explanation   : https://youtu.be/Brt9cWLdLwA

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def getPathFrom(i, j, prevVal):
            if (i < 0) or (j < 0) or (i == m) or (j == n) or (matrix[i][j] <= prevVal):
                return 0

            if (paths[i][j] != 0):
                return paths[i][j]

            paths[i][j] = 1 + \
                max([getPathFrom(i+x, j+y, matrix[i][j]) for x, y in dirs])
            return paths[i][j]

        longestPath = 0
        m, n = len(matrix), len(matrix[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            for j in range(n):
                currentPath = getPathFrom(i, j, -1)
                longestPath = max(longestPath, currentPath)

        return longestPath
