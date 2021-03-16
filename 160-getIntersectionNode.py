# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
双指针法：
一个指针A从headA开始遍历，遍历到尾部后，再从headB开始遍历，遍历到公共节点处停止
一个指针B从headB开始遍历，遍历到尾部后，再从headA开始遍历，遍历到公共节点处停止
路径长度一致，因此如果A==B时，就是有交点，如果没有交点，则此时A指针指向空
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
