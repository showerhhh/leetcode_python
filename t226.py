# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def func(node: TreeNode):
            if node is None:
                return
            func(node.left)
            func(node.right)
            node.left, node.right = node.right, node.left

        func(root)
        return root

    def invertTree_v2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        left = self.invertTree_v2(root.left)
        right = self.invertTree_v2(root.right)
        root.left, root.right = right, left
        return root
