# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # top down dp approach
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum, _ = self.maxPathSumUnder(root)
        return maxPathSum

    def maxPathSumUnder(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        # prevent negative nodes from reporting sums of 0 since null nodes
        # have no paths or branches
        if not root:
            return (float('-inf'), float('-inf'))

        # compute global max path sum under current root by comparing max sum
        # seen within left and right subtrees, and max sum ending at left and
        # right children, and root
        maxLeftPathSum, maxLeftBranchSum = self.maxPathSumUnder(root.left)
        maxRightPathSum, maxRightBranchSum = self.maxPathSumUnder(root.right)

        maxBranchSum = max(root.val, root.val + maxLeftBranchSum, root.val + maxRightBranchSum)
        maxPathSum = max(maxBranchSum, maxLeftPathSum, maxRightPathSum, root.val + maxLeftBranchSum + maxRightBranchSum)

        # report global and local maximum sums at current node
        return (maxPathSum, maxBranchSum)

    # # dfs preorder approach
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     maxPathSum = float('-inf')

    #     # computes only local max path sum ending at node, and updating
    #     # global variable that tracks global max path sum
    #     def maxPathSumAt(root: Optional[TreeNode]) -> int:
    #         nonlocal maxPathSum

    #         if root is None:
    #             return 0

    #         maxSumAtLeft = maxPathSumAt(root.left)
    #         maxSumAtRight = maxPathSumAt(root.right)
    #         maxSumAtCurrent = max(root.val, root.val + maxSumAtLeft + maxSumAtRight, root.val + maxSumAtLeft, root.val + maxSumAtRight)

    #         # update global max path sum if local path sum is larger
    #         maxPathSum = max(maxPathSum, maxSumAtCurrent)

    #         # current node value may be larger local max sum itself versus
    #         # adding a negative max sum from left or right path
    #         return root.val + max(maxSumAtLeft, maxSumAtRight, 0)

    #     maxPathSumAt(root)
    #     return maxPathSum
