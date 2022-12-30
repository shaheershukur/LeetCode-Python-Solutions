# LeetCode Problem Title : 337. House Robber III
# LeetCode Problem Link  : https://leetcode.com/problems/house-robber-iii/
# Solution Explanation   : https://youtu.be/3WaWKRyB5VA

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if not node:
                return (0, 0)
            l = traverse(node.left)
            r = traverse(node.right)
            takingCurnode = node.val + l[1] + r[1]
            notTakingCurNode = max(l[0], l[1]) + max(r[0], r[1])
            return (takingCurnode, notTakingCurNode)

        rootTraversal = traverse(root)
        return max(rootTraversal[0], rootTraversal[1])
