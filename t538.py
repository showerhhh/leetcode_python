# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        count = 0

        def func(node: TreeNode):
            # 中序遍历
            nonlocal count
            if node is None:
                return
            func(node.right)
            temp = node.val
            node.val += count
            count += temp
            func(node.left)

        func(root)
        return root
