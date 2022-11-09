# LeetCode Problem Title : 221. Maximal Square
# LeetCode Problem Link  : https://leetcode.com/problems/maximal-square/
# Solution Explanation   : https://youtu.be/cqPKYGrnXyw

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def getMinimumNeighboringSquare(i, j):
            if ((i == 0) or (j == 0)):
                return 0
            return min(squareSizes[i-1][j], squareSizes[i-1][j-1], squareSizes[i][j-1])

        maxSquareSide = 0
        r, c = len(matrix), len(matrix[0])
        squareSizes = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == "1":
                    squareSizes[i][j] = 1 + getMinimumNeighboringSquare(i, j)
                    maxSquareSide = max(maxSquareSide, squareSizes[i][j])

        return (maxSquareSide * maxSquareSide)
