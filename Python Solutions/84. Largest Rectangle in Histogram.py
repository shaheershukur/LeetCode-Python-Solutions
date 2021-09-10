# LeetCode Problem Title : 84. Largest Rectangle in Histogram
# LeetCode Problem Link  : https://leetcode.com/problems/largest-rectangle-in-histogram/
# Solution Explanation   : https://youtu.be/tkiM_maIkv4

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        left_lim = [0]*n
        right_lim = [0]*n
        left_lim[0] = -1
        right_lim[n-1] = n
        max_area = 0

        for i in range(1, n):
            pointer = i-1
            while (pointer >= 0) and (heights[pointer] >= heights[i]):
                pointer = left_lim[pointer]
            left_lim[i] = pointer

        for i in range(n-2, -1, -1):
            pointer = i+1
            while (pointer < n) and (heights[pointer] >= heights[i]):
                pointer = right_lim[pointer]
            right_lim[i] = pointer

        for i in range(n):
            height = heights[i]
            width = right_lim[i] - left_lim[i] - 1
            area = height*width
            max_area = max(max_area, area)

        return max_area
