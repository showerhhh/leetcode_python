# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        results = []

        def func(node: TreeNode):
            if node is None:
                return
            func(node.left)
            func(node.right)
            results.append(node.val)

        func(root)
        return results
