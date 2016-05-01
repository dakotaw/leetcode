# Given a binary tree, find its maximum depth.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        if right_depth > left_depth:
            return 1 + right_depth
        else:
            return 1 + left_depth