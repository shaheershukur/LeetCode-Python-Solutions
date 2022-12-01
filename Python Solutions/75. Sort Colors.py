# LeetCode Problem Title : 75. Sort Colors
# LeetCode Problem Link  : https://leetcode.com/problems/sort-colors/
# Solution Explanation   : https://youtu.be/_pRSscj5igw

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        red = 0
        pointer = 0
        blue = n-1

        while (pointer <= blue):
            if (nums[pointer] == 0):
                nums[red], nums[pointer] = nums[pointer], nums[red]
                red += 1
                pointer += 1
            elif (nums[pointer] == 2):
                nums[blue], nums[pointer] = nums[pointer], nums[blue]
                blue -= 1
            else:
                pointer += 1
