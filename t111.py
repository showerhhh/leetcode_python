# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        count_list = []  # 保存根节点到所有叶子节点的路径上的节点数量
        count = 1

        def backtracking(node: TreeNode):
            nonlocal count
            if node.left is None and node.right is None:
                count_list.append(count)
                return
            if node.left is not None:
                count += 1
                backtracking(node.left)
                count -= 1
            if node.right is not None:
                count += 1
                backtracking(node.right)
                count -= 1

        if root is None:
            return 0
        else:
            backtracking(root)
            return min(count_list)
