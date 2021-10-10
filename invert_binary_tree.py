# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # post-order traversal and return to parent to swap
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        leftChild = self.invertTree(root.left)
        rightChild = self.invertTree(root.right)

        root.left = rightChild
        root.right = leftChild

        return root

#     # pre-order traversal swapping
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         self.swapLevelNodes(root)
#         return root

#     # pre-order traversal to swap
#     def swapLevelNodes(self, root: Optional[TreeNode]):
#         if root is None:
#             return
    
#         tempLeftChild = root.left
#         root.left = root.right
#         root.right = tempLeftChild

#         self.invertTree(root.left)
#         self.invertTree(root.right)
