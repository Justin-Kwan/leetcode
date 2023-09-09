# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        childrenVals = []
        self.copyChildrenVals(root, childrenVals)
        return childrenVals

    def copyChildrenVals(self, root: TreeNode, childrenVals: List[int]):
        if root == None:
            return

        self.copyChildrenVals(root.left, childrenVals)
        childrenVals.append(root.val)
        self.copyChildrenVals(root.right, childrenVals)

    # iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodeStack = []
        nodeList = []

        # traverse tree, moving right
        while True:
            # traverse down leftmost branch
            while root is not None:
                nodeStack.append(root)  # push each node to stack
                root = root.left
            
            # if no parent/ancestor to go back to, end
            if not nodeStack:
                return nodeList
            
            # replace null node with last parent/ancestor in stack
            root = nodeStack.pop()
            nodeList.append(root.val)
            root = root.right
            
