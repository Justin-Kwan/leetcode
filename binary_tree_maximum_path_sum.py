# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxPathSumSoFar: int = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPathSum(root)
        return self.maxPathSumSoFar

    def findMaxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxSumUpToLeft = self.findMaxPathSum(root.left)
        maxSumUpToRight = self.findMaxPathSum(root.right)
        maxSumUpToCurrent = max(root.val, root.val + maxSumUpToLeft + maxSumUpToRight, root.val + maxSumUpToLeft, root.val + maxSumUpToRight)

        # update global max path sum if local path sum is larger
        self.maxPathSumSoFar = max(self.maxPathSumSoFar, maxSumUpToCurrent)

        # prevent "forcing" current node val to sum if left or right is negative
        # current node can always skip summing with max up to left or right
        return root.val + max(maxSumUpToLeft, maxSumUpToRight, 0)
