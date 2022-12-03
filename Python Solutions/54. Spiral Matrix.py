# LeetCode Problem Title : 54. Spiral Matrix
# LeetCode Problem Link  : https://leetcode.com/problems/spiral-matrix/
# Solution Explanation   : https://youtu.be/2J6paJcM710

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def insideMatrixAndNotNone(i, j):
            return (0 <= i < m) and (0 <= j < n) and (matrix[i][j] != None)

        m, n = len(matrix), len(matrix[0])
        result = []
        i, j = 0, 0
        diri, dirj = 0, 1

        while True:
            result.append(matrix[i][j])
            matrix[i][j] = None

            nexti = i + diri
            nextj = j + dirj
            if insideMatrixAndNotNone(nexti, nextj):
                i = nexti
                j = nextj
            else:
                diri, dirj = dirj, -diri
                i += diri
                j += dirj
                if not insideMatrixAndNotNone(i, j):
                    break

        return result
