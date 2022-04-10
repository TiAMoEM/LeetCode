# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return last
