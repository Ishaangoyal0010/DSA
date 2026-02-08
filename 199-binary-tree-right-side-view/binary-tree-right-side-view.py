class Solution(object):
    def solve(self,root,depth,result):
        if root==None:
            return

        if len(result)==depth:
            result.append(root.val)

        self.solve(root.right,depth+1,result)
        self.solve(root.left,depth+1,result)

    def rightSideView(self, root):
        result=[]
        self.solve(root,0,result)
        return result

