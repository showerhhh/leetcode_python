# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            elif node1.val == node2.val and func(node1.left, node2.right) and func(node1.right, node2.left):
                return True

        if root is None:
            return True
        else:
            return func(root.left, root.right)
