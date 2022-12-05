# LeetCode Problem Title : 59. Spiral Matrix II
# LeetCode Problem Link  : https://leetcode.com/problems/spiral-matrix-ii/
# Solution Explanation   : https://youtu.be/FQEY9qImr0E

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        def insideMatrixAndNotUsed(i, j):
            return (0 <= i < n) and (0 <= j < n) and (matrix[i][j] == None)

        matrix = [[None for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        diri, dirj = 0, 1
        counter = 1

        while True:
            matrix[i][j] = counter
            counter += 1

            nexti = i + diri
            nextj = j + dirj
            if insideMatrixAndNotUsed(nexti, nextj):
                i = nexti
                j = nextj
            else:
                diri, dirj = dirj, -diri
                i += diri
                j += dirj
                if not insideMatrixAndNotUsed(i, j):
                    break

        return matrix
