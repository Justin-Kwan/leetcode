# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # optimal (preorder traversal)
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidSubtree(root, float('-inf'), float('inf'))
    
    def isValidSubtree(self, root: TreeNode, lowerBound: int, upperBound: int) -> bool:
        if root == None:
            return True

        isValidChild = lowerBound < root.val and root.val < upperBound

        # traverse left => current should be upper bound
        # traverse right => current should be lower bound
        return isValidChild and self.isValidSubtree(root.left, lowerBound, root.val) and self.isValidSubtree(root.right, root.val, upperBound)

