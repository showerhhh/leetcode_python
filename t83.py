# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = head
        q = head.next
        while q is not None:
            if q.val == p.val:
                q = q.next
            else:
                p.next = q
                p = q
                q = q.next
        p.next = None
        return head
