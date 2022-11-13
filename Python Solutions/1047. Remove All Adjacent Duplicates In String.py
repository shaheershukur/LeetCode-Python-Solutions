# LeetCode Problem Title : 1047. Remove All Adjacent Duplicates In String
# LeetCode Problem Link  : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Solution Explanation   : https://youtu.be/2J79Lwu3o-c

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for letter in s:
            if (len(stack) == 0):
                stack.append(letter)
            else:
                if (stack[-1] != letter):
                    stack.append(letter)
                else:
                    stack.pop()

        return "".join(stack)
