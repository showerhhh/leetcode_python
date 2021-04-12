# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        p = head
        q = head.next
        while p != q:
            if q is None or q.next is None:
                return False
            p = p.next
            q = q.next.next
        return True
