# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     # dfs write to list by recursion depth index
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         nodesByLevel: List[List[int]] = []
#         self.encodeNodesByLevel(root, nodesByLevel, 0)
#         return nodesByLevel

#     def encodeNodesByLevel(self, root: Optional[TreeNode], nodesByLevel: List[List[int]], levelIndex: int):
#         if not root:
#             return

#         if len(nodesByLevel) <= levelIndex:
#             nodesByLevel.append([])

#         nodesByLevel[levelIndex].append(root.val)

#         self.encodeNodesByLevel(root.left, nodesByLevel, levelIndex + 1)
#         self.encodeNodesByLevel(root.right, nodesByLevel, levelIndex + 1)

    # bfs approach, queue each level's nodes and copy to result
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodesToVisit = collections.deque([root])
        nodesByLevel = []

        while nodesToVisit:
            # take size snapshot of current level
            levelSize = len(nodesToVisit)
            
            # copy level's node values to result set
            levelNodeValues = []
            for node in nodesToVisit:
                levelNodeValues.append(node.val)

            nodesByLevel.append(levelNodeValues)

            # replace current level up to snapshot size with next level's nodes
            for _ in range(0, levelSize):
                currNode = nodesToVisit.popleft()

                if currNode.left:
                    nodesToVisit.append(currNode.left)
                if currNode.right:
                    nodesToVisit.append(currNode.right)

        return nodesByLevel
