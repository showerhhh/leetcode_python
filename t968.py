# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        count = 0

        def lrd(node: TreeNode) -> int:
            # 后根遍历，并返回根节点状态
            # 有三个状态:
            # 0 = > 这个结点待覆盖
            # 1 = > 这个结点已经覆盖
            # 2 = > 这个结点上安装了相机
            nonlocal count
            if node is None:
                return 1
            left = lrd(node.left)
            right = lrd(node.right)
            if left == 0 or right == 0:
                count += 1
                return 2
            elif left == 1 and right == 1:
                return 0
            else:
                return 1

        if lrd(root) == 0:
            count += 1
        return count
