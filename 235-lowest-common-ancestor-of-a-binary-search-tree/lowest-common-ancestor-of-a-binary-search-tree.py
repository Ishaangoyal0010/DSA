class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while True:
            if q.val>root.val and p.val>root.val:
                root=root.right
            elif q.val<root.val and p.val<root.val:
                root=root.left  
            else:
                return root
        return -1
        