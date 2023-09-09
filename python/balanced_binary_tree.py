# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if is unbalanced tree (not an AVL), then height is -1
        return self.countSubtreeHeight(root) >= 0

    def countSubtreeHeight(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxLeftHeight = self.countSubtreeHeight(root.left)
        maxRightHeight = self.countSubtreeHeight(root.right)

        # if left or right subtrees are unbalanced, propogate
        if maxLeftHeight == -1 or maxRightHeight == -1:
            return -1
        # if tree at current node is unbalanced, while left and right subtrees are balanced
        if abs(maxLeftHeight - maxRightHeight) > 1:
            return -1

        return max(maxLeftHeight, maxRightHeight) + 1
