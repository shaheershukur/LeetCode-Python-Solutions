# LeetCode Problem Title : 213. House Robber II
# LeetCode Problem Link  : https://leetcode.com/problems/house-robber-ii/
# Solution Explanation   : https://youtu.be/NhZsWqyMYj0

class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouses(houses):
            n = len(houses)
            if (n == 1):
                return houses[0]
            dp = [0]*n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            return dp[-1]

        if (len(nums) <= 2):
            return max(nums)
        return max(robHouses(nums[1:]), robHouses(nums[:-1]))
