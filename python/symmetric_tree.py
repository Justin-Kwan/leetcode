# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.doSubtreesMirror(root.left, root.right)

    def doSubtreesMirror(self, leftRoot: TreeNode, rightRoot: TreeNode):
        if leftRoot is None and rightRoot is None:
            return True

        # at most one is null
        if leftRoot is None or rightRoot is None or leftRoot.val != rightRoot.val:
            return False
        
        # else if they match
        return self.doSubtreesMirror(leftRoot.left, rightRoot.right) and self.doSubtreesMirror(leftRoot.right, rightRoot.left)

