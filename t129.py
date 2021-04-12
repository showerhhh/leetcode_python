# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0

        def func(node: TreeNode, digit: int):
            nonlocal result
            digit = digit * 10 + node.val
            if node.left is None and node.right is None:
                result += digit
                return
            if node.left is not None:
                func(node.left, digit)
            if node.right is not None:
                func(node.right, digit)

        if root is None:
            return 0
        else:
            func(root, 0)
            return result
