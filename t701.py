# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def func(node: TreeNode) -> TreeNode:
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = func(node.left)
            else:
                node.right = func(node.right)
            return node

        return func(root)
