from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode):
        count = defaultdict(int)

        def func(node: TreeNode):
            if node is None:
                return
            count[node.val] += 1
            func(node.left)
            func(node.right)

        if root is None:
            return []
        func(root)
        max_val = max(count.values())
        result = []
        for key, val in count.items():
            if val == max_val:
                result.append(key)
        return result
