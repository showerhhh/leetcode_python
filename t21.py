# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        while l1 is not None:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2 is not None:
            p.next = l2
            p = p.next
            l2 = l2.next

        return head.next  # 去掉头结点
