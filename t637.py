# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode):
        queue = [root]
        results = []

        while queue:
            sum = 0
            count = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                sum += node.val
                count += 1
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            results.append(sum / count)

        return results
