# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # optimal dfs approach
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # next inorder successor is initally null, which could be replaced
        # while backtracking to first ancestor node larger than target
        if not root:
            return None

        inorderSuccessor = None

        # target node could exist in left or right subtree
        if p.val < root.val:
            inorderSuccessor = self.inorderSuccessor(root.left, p)
        else:
            inorderSuccessor = self.inorderSuccessor(root.right, p)

        # next largest node could be above target node, so replace with it
        # while backtracking
        if not inorderSuccessor and root.val > p.val:
            inorderSuccessor = root

        return inorderSuccessor
