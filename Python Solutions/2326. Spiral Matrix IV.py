# LeetCode Problem Title : 2326. Spiral Matrix IV
# LeetCode Problem Link  : https://leetcode.com/problems/spiral-matrix-iv/
# Solution Explanation   : https://youtu.be/U4Tnms16Imk

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        def insideMatrixAndNotUsed(i, j):
            return (0 <= i < m) and (0 <= j < n) and (matrix[i][j] == -1)

        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        diri, dirj = 0, 1

        while head:
            matrix[i][j] = head.val
            head = head.next

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
