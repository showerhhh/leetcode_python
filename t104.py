# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def func(node: TreeNode) -> 0:
            if node is None:
                return 0
            left_depth = func(node.left)
            right_depth = func(node.right)
            return max(left_depth, right_depth) + 1
        return func(root)
