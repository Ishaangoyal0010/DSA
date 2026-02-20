class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        curr =root
        while True:
            if q.val>curr.val and p.val>curr.val:
                curr=curr.right
            elif q.val<curr.val and p.val<curr.val:
                curr=curr.left  
            else:
                return curr
        return -1
        