# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        empty = ListNode(-1)
        empty.next = head
        if empty.next is None or empty.next.next is None:
            return empty.next
        previous = empty
        p = empty.next
        q = empty.next.next
        while p is not None and q is not None:
            # 交换
            p.next = q.next
            q.next = p
            previous.next = q
            # 移动三个指针
            previous = p
            if previous.next is None or previous.next.next is None:
                break
            p = previous.next
            q = previous.next.next
        return empty.next
