# LeetCode Problem Title : 152. Maximum Product Subarray
# LeetCode Problem Link  : https://leetcode.com/problems/maximum-product-subarray/
# Solution Explanation   : https://youtu.be/hbzPkxYfGbk

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0]*n
        dp[0] = (nums[0], nums[0])

        mxprod = nums[0]

        for i in range(1, n):
            max_positive = max(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            max_negative = min(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            dp[i] = (max_positive, max_negative)
            mxprod = max(mxprod, max_positive)

        return mxprod
