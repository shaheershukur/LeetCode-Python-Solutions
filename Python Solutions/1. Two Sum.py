# LeetCode Problem Title : 1. Two Sum
# LeetCode Problem Link  : https://leetcode.com/problems/two-sum/
# Solution Explanation   : https://youtu.be/LVSE4e4IYmE

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = dict()

        for index, value in enumerate(nums):
            remaining_number = target - value

            if remaining_number in index_map:
                return [index_map[remaining_number], index]

            index_map[value] = index
