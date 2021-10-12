# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     # dfs approach postorder traversal (time: O(N) where N is number of children, space: O(N), where N is number of children) 
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # bfs approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodesToVisit = collections.deque([root])
        maxDepthSoFar = 0

        while nodesToVisit:
            levelNodeCount = len(nodesToVisit)

            # iterate through all nodes in current level
            for _ in range(0, levelNodeCount):
                currNode = nodesToVisit.popleft()
                
                if currNode.left:
                    nodesToVisit.append(currNode.left)
                if currNode.right:
                    nodesToVisit.append(currNode.right)

            maxDepthSoFar += 1

        return maxDepthSoFar
