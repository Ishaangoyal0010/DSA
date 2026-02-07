class Solution(object):
    def solve(self, root):
        if root == None:
            return 0
        leftheight = self.solve(root.left)
        rightheight = self.solve(root.right)
        self.diameter = max(self.diameter, leftheight + rightheight)
        return 1 + max(leftheight, rightheight)   
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.solve(root)
        return self.diameter