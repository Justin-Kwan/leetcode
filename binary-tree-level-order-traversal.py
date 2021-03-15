k# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs preorder traversal
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        childrenAtDepthLookup: Dict[int, List[int]] = {}

        self.organizeChildrenByDepth(root, childrenAtDepthLookup, 0)

        childrenAtDepth = []

        for depth in childrenAtDepthLookup:
            childrenAtDepth.append(childrenAtDepthLookup[depth])

        return childrenAtDepth

    def organizeChildrenByDepth(self, root: TreeNode, childrenAtDepthLookup: Dict[int, List[int]], currDepth: int):
        
        if root == None:
            return

        if currDepth not in childrenAtDepthLookup:
            childrenAtDepthLookup[currDepth] = []

        childrenAtDepthLookup[currDepth].append(root.val)

        self.organizeChildrenByDepth(root.left, childrenAtDepthLookup, currDepth + 1)
        self.organizeChildrenByDepth(root.right, childrenAtDepthLookup, currDepth + 1)

