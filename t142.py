# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        count = set()
        p = head
        while p is not None:
            if p in count:
                return p
            else:
                count.update([p])
            p = p.next
        return None
