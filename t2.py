# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        carry = 0
        result = ListNode(-1)  # 头结点
        k = result
        while p is not None and q is not None:
            temp = p.val + q.val + carry
            k.next = ListNode(temp % 10)
            carry = temp // 10
            p = p.next
            q = q.next
            k = k.next
        while p is not None:
            temp = p.val + carry
            k.next = ListNode(temp % 10)
            carry = temp // 10
            p = p.next
            k = k.next
        while q is not None:
            temp = q.val + carry
            k.next = ListNode(temp % 10)
            carry = temp // 10
            q = q.next
            k = k.next
        if carry > 0:
            k.next = ListNode(carry)
        return result.next
