# LeetCode Problem Title : 169. Majority Element
# LeetCode Problem Link  : https://leetcode.com/problems/majority-element/
# Solution Explanation   : https://youtu.be/2wX-X76THKI

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums).most_common()
        return c[0][0]
