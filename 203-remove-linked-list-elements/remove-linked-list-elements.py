# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
       prev=None 
       curr=head
       while curr:
        if head.val==val:
            head=head.next
            curr=head
            continue
        if curr.val==val:
            prev.next=curr.next
            curr=curr.next
        else:
            prev=curr
            curr=curr.next
       return head 
        