import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        results = []
        result = []
        count = 0

        def backtracking(node: TreeNode):
            nonlocal count
            if node.left is None and node.right is None:
                result.append(node.val)
                count += node.val
                if count == sum:
                    results.append(copy.deepcopy(result))
                count -= node.val
                result.pop()
                return
            result.append(node.val)
            count += node.val
            if node.left is not None:
                backtracking(node.left)
            if node.right is not None:
                backtracking(node.right)
            count -= node.val
            result.pop()

        if root is None:
            return []
        backtracking(root)
        return results
