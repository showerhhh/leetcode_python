# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []

        def func(node: TreeNode):
            if node is None:
                return
            func(node.left)
            result.append(node.val)
            func(node.right)

        func(root)
        return result
