# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ldr = []

        def func(node: TreeNode):
            if node is None:
                return
            func(node.left)
            ldr.append(node.val)
            func(node.right)

        func(root)
        result = ldr[1] - ldr[0]
        for i in range(2, len(ldr)):
            temp = ldr[i] - ldr[i - 1]
            if temp < result:
                result = temp
        return result
