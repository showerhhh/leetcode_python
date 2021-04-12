# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        empty = ListNode(-1)
        empty.next = head
        p = empty
        q = empty
        for i in range(n + 1):
            p = p.next
        while p is not None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return empty.next
