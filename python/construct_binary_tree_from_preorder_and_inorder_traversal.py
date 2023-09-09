# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # optimal walking root index approach
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildSubtree(left: int, right: int):
            nonlocal preorderRootPos

            # given left or right subtree is empty, reached null node
            if left > right:
                return None

            # walk to next node's position in preorder traversal, either left subtree root
            # or right subtree root
            preorderRootPos += 1
            rootVal = preorder[preorderRootPos]
            inorderRootPos = inorderPositions[rootVal]

            # construct subtree of current root
            return TreeNode(rootVal, buildSubtree(left, inorderRootPos - 1), buildSubtree(inorderRootPos + 1, right))

        # globally (within nested scope) walk root node position in preorder traversal
        preorderRootPos = -1

        if not preorder or not inorder:
            return None

        inorderPositions = {}
        for i in range(len(inorder)):
            inorderPositions[inorder[i]] = i

        return buildSubtree(0, len(inorder) - 1)
