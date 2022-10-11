# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # optimal (preorder traversal)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubtree(root, float("-inf"), float("inf"))

    def isValidSubtree(self, root: Optional[TreeNode], lowerBound: int, upperBound: int) -> bool:
        if not root:
            return True

        # root is out of range of parent nodes' values
        if root.val <= lowerBound or root.val >= upperBound:
            return False

        return self.isValidSubtree(root.left, lowerBound, root.val) and self.isValidSubtree(root.right, root.val, upperBound)
