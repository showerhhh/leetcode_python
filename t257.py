# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        # 分治
        result_list = []

        def func(node: TreeNode, path: str):
            if node is None:
                return
            if node.left is None and node.right is None:
                path = path + str(node.val)
                result_list.append(path)
                return
            path = path + str(node.val) + '->'
            func(node.left, path)
            func(node.right, path)
            return

        func(root, '')
        return result_list

    def binaryTreePaths_2(self, root: TreeNode):
        # 回溯
        result = []
        path = []

        def backtracking(node: TreeNode):
            if node.left is None and node.right is None:
                path.append(str(node.val))
                result.append('->'.join(path))
                path.pop()
                return

            not_none_child_list = []
            if node.left is not None:
                not_none_child_list.append(node.left)
            if node.right is not None:
                not_none_child_list.append(node.right)

            path.append(str(node.val))
            for i in not_none_child_list:
                backtracking(i)
            path.pop()

        if root is None:
            return []
        else:
            backtracking(root)
            return result
