# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def func(node: TreeNode) -> int:
            # 返回以node为根节点的树的左叶子之和
            if node is None:
                return 0
            if node.left is not None and node.left.left is None and node.left.right is None:
                return node.left.val + func(node.right)
            nums1 = func(node.left)
            nums2 = func(node.right)
            return nums1 + nums2

        return func(root)
