# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        # 统计链表总长度
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next

        # 让p指向后半部分的第一个结点
        h2_len = n // 2 if n % 2 == 1 else n // 2 - 1  # 后半部分的长度
        p = head
        for i in range(n - h2_len - 1):
            p = p.next
        k = p.next
        p.next = None
        p = k

        # 后半部分使用头插法构成h2
        h2_empty = ListNode(-1)
        while p is not None:
            temp = p.next
            p.next = h2_empty.next
            h2_empty.next = p
            p = temp

        # 将h2合并进前半部分
        p = head
        q = h2_empty.next
        while q is not None:
            h2_empty.next = q.next
            q.next = p.next
            p.next = q
            p = q.next
            q = h2_empty.next
