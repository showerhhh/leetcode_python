# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        empty_input = ListNode(-1, head)
        empty_odd = ListNode(-1, None)
        last_odd = empty_odd  # 尾结点指针
        empty_even = ListNode(-1, None)
        last_even = empty_even  # 尾结点指针
        flag = 1
        p = empty_input.next
        while p is not None:
            if flag == 1:
                # 奇数结点
                empty_input.next = p.next
                last_odd.next = p
                p.next = None
                last_odd = last_odd.next
                p = empty_input.next
            else:
                # 偶数结点
                empty_input.next = p.next
                last_even.next = p
                p.next = None
                last_even = last_even.next
                p = empty_input.next
            flag = (flag + 1) % 2
        last_odd.next = empty_even.next
        return empty_odd.next
