# LeetCode Problem Title : 885. Spiral Matrix III
# LeetCode Problem Link  : https://leetcode.com/problems/spiral-matrix-iii/
# Solution Explanation   : https://youtu.be/J5Duze0IgII

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        matrix = [[None for _ in range(cols)] for _ in range(rows)]
        i, j = rStart, cStart
        result = [[i, j]]
        diri, dirj = 0, 1
        totalCells = 1
        twiceCounter = 2
        nextRoundTotalCells = 2

        while True:
            if (len(result) == (rows*cols)):
                break

            i += diri
            j += dirj
            if (0 <= i < rows) and (0 <= j < cols):
                result.append([i, j])

            totalCells -= 1
            if (totalCells == 0):
                diri, dirj = dirj, -diri
                twiceCounter -= 1
                if (twiceCounter == 0):
                    twiceCounter = 2
                    totalCells = nextRoundTotalCells
                    nextRoundTotalCells += 1
                else:
                    totalCells = nextRoundTotalCells - 1

        return result
