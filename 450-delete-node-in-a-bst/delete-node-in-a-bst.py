# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        # Find the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            
            # Case 1: Node has no children (leaf)
            if root.left is None and root.right is None:
                return None
            
            # Case 2: Node has only right child
            if root.left is None:
                return root.right
            
            # Case 3: Node has only left child
            if root.right is None:
                return root.left
            
            # Case 4: Node has both children
            # Find inorder successor (smallest in right subtree)
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        
        return root
        