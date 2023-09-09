# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodeVals = []
        self.encodeBSTInorder(root, nodeVals)

        return self.buildBalancedBST(nodeVals, 0, len(nodeVals) - 1)

    def encodeBSTInorder(self, root: TreeNode, encodedBST):
        if not root:
            return

        self.encodeBSTInorder(root.left, encodedBST)
        encodedBST.append(root.val)
        self.encodeBSTInorder(root.right, encodedBST)

    def buildBalancedBST(self, nodeVals: List[int], start: int, end: int) -> TreeNode:
        # empty list, no more nodes to insert
        if end < start:
            return None

        # root is median of sorted list
        middle = (start + end) // 2
        root = TreeNode(nodeVals[middle])

        # attach left subtree (with median of left sublist as root) and
        # right subtree (with median of right sublist as root)
        root.left = self.buildBalancedBST(nodeVals, start, middle - 1)
        root.right = self.buildBalancedBST(nodeVals, middle + 1, end)

        return root
