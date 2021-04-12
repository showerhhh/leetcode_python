# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        result = []

        def func(node: TreeNode):
            if node is None:
                return
            result.append(node.val)
            func(node.left)
            func(node.right)

        func(root)
        return result
