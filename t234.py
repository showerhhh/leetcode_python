# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        my_list = []
        p = head
        while p:
            my_list.append(p.val)
            p = p.next
        i = 0
        n = len(my_list)
        while i < n // 2:
            if my_list[i] == my_list[n - 1 - i]:
                i += 1
            else:
                return False
        return True
