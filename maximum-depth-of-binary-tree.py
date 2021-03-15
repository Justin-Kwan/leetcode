# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # postorder traversal (time: O(N) where N is number of children, space: O(N), where N is number of children) 
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0 # TODO: check!

        currMaxDepth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return currMaxDepth

