# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     # preorder traversal swapping
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         self.invertSubtree(root)
#         return root

#     def invertSubtree(self, root: Optional[TreeNode]) -> None:
#         if not root:
#             return

#         # swap left and right subtrees, and continue swapping in both
#         root.left, root.right = root.right, root.left

#         self.invertSubtree(root.left)
#         self.invertSubtree(root.right)

    # postorder traversal and return parent to swap
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        invertedRight = self.invertTree(root.right)
        invertedLeft = self.invertTree(root.left)

        root.left = invertedRight
        root.right = invertedLeft

        return root
