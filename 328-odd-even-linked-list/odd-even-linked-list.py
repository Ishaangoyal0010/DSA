# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head== None or head.next==None:
            return head
        else:
            odd=head
            even = head.next
            temp=head.next
            while even is not None and even.next is not None:
                odd.next=odd.next.next
                odd=odd.next
                even.next=even.next.next
                even=even.next
            odd.next=temp
            return head

        