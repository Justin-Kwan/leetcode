# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # hit bottom of branch with no matching subtree along the way
        if root is None:
            return False

        if self.doTreesMatch(root, subRoot):
            return True

        # recenter main root for subroot to compare with left and right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def doTreesMatch(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        # if either main tree or subtree node is null and other isn't
        if root is None or subRoot is None:
            return False

        # at current fixed node "root", is "subRoot" a subtree?
        return root.val == subRoot.val and self.doTreesMatch(root.left, subRoot.left) and self.doTreesMatch(root.right, subRoot.right)
