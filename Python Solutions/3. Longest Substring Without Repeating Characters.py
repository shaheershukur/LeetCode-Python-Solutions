# LeetCode Problem Title : 3. Longest Substring Without Repeating Characters
# LeetCode Problem Link  : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solution Explanation   : https://youtu.be/glxWk6AZS5M

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if (n <= 1):
            return n

        maxLength = 0

        i, j = 0, 0
        charFoundIndex = dict()
        while j < n:
            if s[j] in charFoundIndex:
                i = max(i, charFoundIndex[s[j]]+1)
            charFoundIndex[s[j]] = j
            maxLength = max(maxLength, j-i+1)
            j += 1

        return maxLength
