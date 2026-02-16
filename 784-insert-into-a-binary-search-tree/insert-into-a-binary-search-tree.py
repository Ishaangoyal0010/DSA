# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        temp=root
        if root is None:
            return TreeNode(val)
        while True:
            if val < root.val:
                if root.left is None:
                    root.left=TreeNode(val)
                    break
                root=root.left
            if val > root.val:
                if root.right is None:
                    root.right=TreeNode(val)
                    break
                root=root.right
        return temp