# LeetCode Problem Title : 62. Unique Paths
# LeetCode Problem Link  : https://leetcode.com/problems/unique-paths/
# Solution Explanation   : https://youtu.be/2Ws2ME9yoEc

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def getTotalPaths(r, c):
            if (r, c) in cache:
                return cache[(r, c)]

            if (r >= m) or (c >= n):
                return 0

            if (r == (m-1)) and (c == (n-1)):
                return 1

            cache[(r, c)] = getTotalPaths(r, c+1) + getTotalPaths(r+1, c)
            return cache[(r, c)]

        cache = dict()
        paths = getTotalPaths(0, 0)
        return paths
