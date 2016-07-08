# Given a binary tree, return the preorder traversal of its nodes' values.
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 8th percentile

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        output = [root.val]
        output.extend(self.preorderTraversal(root.left))
        output.extend(self.preorderTraversal(root.right))
        return output