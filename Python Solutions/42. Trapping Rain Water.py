# LeetCode Problem Title : 42. Trapping Rain Water
# LeetCode Problem Link  : https://leetcode.com/problems/trapping-rain-water/
# Solution Explanation   : https://youtu.be/nwdM2htNgNw

class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0
        n = len(height)
        lim_bars = [[0, 0] for _ in range(n)]

        for i in range(1, n-1):
            lim_bars[i][0] = max(height[i-1], lim_bars[i-1][0])

        for i in range(n-2, 0, -1):
            lim_bars[i][1] = max(height[i+1], lim_bars[i+1][1])

        for i in range(1, n-1):
            water_level = min(lim_bars[i])
            if height[i] < water_level:
                total_water += water_level - height[i]

        return total_water
