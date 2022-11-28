# LeetCode Problem Title : 236. Lowest Common Ancestor of a Binary Tree
# LeetCode Problem Link  : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Solution Explanation   : https://youtu.be/91jwWzvBreo

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traverse(node):
            nonlocal lowestCommonAncestor
            if (not node) or (lowestCommonAncestor):
                return 0

            leftNode = traverse(node.left)
            rightNode = traverse(node.right)

            currNode = 1 if ((node == p) or (node == q)) else 0
            if ((currNode + leftNode + rightNode) == 2):
                lowestCommonAncestor = node

            return 1 if (currNode or leftNode or rightNode) else 0

        lowestCommonAncestor = None
        traverse(root)
        return lowestCommonAncestor
