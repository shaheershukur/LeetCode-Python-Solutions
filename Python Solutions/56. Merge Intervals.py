# LeetCode Problem Title : 56. Merge Intervals
# LeetCode Problem Link  : https://leetcode.com/problems/merge-intervals/
# Solution Explanation   : https://youtu.be/iD68J9FdfVg

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals:
            if (start <= merged[-1][1]):
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged
