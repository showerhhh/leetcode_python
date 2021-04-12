# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def func(inorder_start, inorder_end, postorder_start, postorder_end) -> TreeNode:
            if inorder_end < inorder_start or postorder_end < postorder_start:
                return None
            node = TreeNode(postorder[postorder_end])
            index = inorder.index(postorder[postorder_end])
            len_left_tree = index - inorder_start
            node.left = func(inorder_start, index-1, postorder_start, postorder_start+len_left_tree-1)
            node.right = func(index+1, inorder_end, postorder_start+len_left_tree, postorder_end-1)
            return node

        return func(0, len(inorder)-1, 0, len(postorder)-1)
