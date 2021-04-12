# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q) -> TreeNode:
        def func(node: TreeNode) -> TreeNode:
            if node.val > p.val and node.val > q.val:
                return func(node.left)
            if node.val < p.val and node.val < q.val:
                return func(node.right)
            return node

        return func(root)
