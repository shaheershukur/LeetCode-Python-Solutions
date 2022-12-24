# LeetCode Problem Title : 2078. Two Furthest Houses With Different Colors
# LeetCode Problem Link  : https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# Solution Explanation   : https://youtu.be/DNwy6NcLj3k

class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        n = len(colors)
        maxDistance = 0

        for i in range(n):
            distanceFromLeftMost = i if(colors[i] != colors[0]) else 0
            distanceFromRightMost = (n-1-i) if(colors[i] != colors[n-1]) else 0
            maxDistance = max(
                maxDistance, distanceFromLeftMost, distanceFromRightMost)

        return maxDistance
