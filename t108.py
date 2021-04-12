# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def func(left, right) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = func(left, mid - 1)
            node.right = func(mid + 1, right)
            return node

        return func(0, len(nums) - 1)
