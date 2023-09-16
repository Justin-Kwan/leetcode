# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     dfs preorder traversal using map
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         childrenAtDepthLookup: Dict[int, List[int]] = {}

#         self.organizeChildrenByDepth(root, childrenAtDepthLookup, 0)
#         childrenAtDepth = []

#         for depth in childrenAtDepthLookup:
#             childrenAtDepth.append(childrenAtDepthLookup[depth])

#         return childrenAtDepth

#     def organizeChildrenByDepth(self, root: TreeNode, childrenAtDepthLookup: Dict[int, List[int]], currDepth: int):
#         if root == None:
#             return
#
#         if currDepth not in childrenAtDepthLookup:
#             childrenAtDepthLookup[currDepth] = []

#         childrenAtDepthLookup[currDepth].append(root.val)

#         self.organizeChildrenByDepth(root.left, childrenAtDepthLookup, currDepth + 1)
#         self.organizeChildrenByDepth(root.right, childrenAtDepthLookup, currDepth + 1)

#     # cleaner dfs write to list by recursion depth index
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
            nodeLevelValues = []

            # replace current level up to snapshot size with next level's nodes
            for _ in range(levelSize):
                curNode = nodesToVisit.popleft()
                nodeLevelValues.append(curNode.val)

                if curNode.left:
                    nodesToVisit.append(curNode.left)
                if curNode.right:
                    nodesToVisit.append(curNode.right)

            nodesByLevel.append(nodeLevelValues)

        return nodesByLevel
