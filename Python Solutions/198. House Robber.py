# LeetCode Problem Title : 198. House Robber
# LeetCode Problem Link  : https://leetcode.com/problems/house-robber/
# Solution Explanation   : https://youtu.be/Yhm6Y8trVn4

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if (n == 1):
            return nums[0]

        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            firstAndThird = dp[i-2] + nums[i]
            second = dp[i-1]
            dp[i] = max(firstAndThird, second)

        return dp[-1]
