# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self, root):
        if root==None:
            return 0
        leftheight=self.solve(root.left)
        rightheight=self.solve(root.right)
        return 1 + max(leftheight,rightheight)
    def maxDepth(self, root):
        result = self.solve(root)
        return result
        
        