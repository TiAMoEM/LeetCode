# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        q = head.next
        while p != None and q != None:
            if p.val != q.val:
                p = q
                q = q.next
            else:
                p.next = q.next
                q = q.next
        return head