# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ListNode(None)
        p.next = head
        q = p
        while q.next != None:
            if q.next.val == val:
                q.next = q.next.next
            else:
                q = q.next
        return p.next