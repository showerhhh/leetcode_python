# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root is None:
            return []

        results = []
        queue = [root]

        while queue:
            one_level = list()
            size = len(queue)  # 控制一次while循环拿出几个节点
            for i in range(size):
                node = queue.pop(0)
                one_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(one_level)

        return results[::-1]
