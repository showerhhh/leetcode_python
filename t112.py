# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def func(node: TreeNode, sum: int):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val == sum
            return func(node.left, sum - node.val) or func(node.right, sum - node.val)
        return func(root, sum)
