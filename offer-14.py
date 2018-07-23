# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < k or k < 1:
            return None
        return l[-k]