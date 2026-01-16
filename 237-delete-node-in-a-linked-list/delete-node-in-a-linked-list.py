# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
         while node:
            node.val=node.next.val
            if node.next.next is None:
                node.next=None
            node=node.next
        