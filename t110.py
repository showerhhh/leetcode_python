# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = True

        def func(node: TreeNode) -> int:
            nonlocal flag
            if node is None:
                return 0
            left = func(node.left)
            right = func(node.right)
            if abs(left - right) > 1:
                flag = False
            return max(left, right) + 1

        func(root)
        return flag
