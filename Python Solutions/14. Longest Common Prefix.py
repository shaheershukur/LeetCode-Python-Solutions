# LeetCode Problem Title : 14. Longest Common Prefix
# LeetCode Problem Link  : https://leetcode.com/problems/longest-common-prefix/
# Solution Explanation   : https://youtu.be/qyTIu2vfWq4

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        if (n < 2):
            return strs[0]

        commonPrefix = []

        for charIndex, char in enumerate(strs[0]):
            needToTerminate = False
            for i in range(1, n):
                if ((charIndex == len(strs[i])) or (char != strs[i][charIndex])):
                    needToTerminate = True
                    break
            if (needToTerminate):
                break
            commonPrefix.append(char)

        return "".join(commonPrefix)
