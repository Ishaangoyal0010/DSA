class Solution(object):
    def solve(self, root):
        if root == None:
            return 0
        
        leftheight = max(0, self.solve(root.left))
        rightheight = max(0, self.solve(root.right))
        self.diameter = max(self.diameter, leftheight + rightheight + root.val)
        return root.val + max(leftheight, rightheight)
    
    def maxPathSum(self, root):
        self.diameter = float('-inf')
        self.solve(root)
        return self.diameter