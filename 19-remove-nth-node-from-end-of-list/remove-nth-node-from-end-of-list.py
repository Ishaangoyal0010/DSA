class Solution(object):
    def removeNthFromEnd(self, head, n):
        cnt = 0
        temp = head

        while temp:
            cnt += 1
            temp = temp.next

        # If removing the head node
        if n == cnt:
            return head.next   # ❗ fix here

        move = cnt - n
        temp = head

        for _ in range(move - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head
