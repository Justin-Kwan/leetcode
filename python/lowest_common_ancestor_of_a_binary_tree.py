# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lca: TreeNode = None

    # optimal dfs
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.containsPq(root, p, q)
        return self.lca

    def containsPq(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not root:
            return False

        # if root is p or q
        isRoot = root.val == q.val or root.val == p.val

        # if left subtree contains p or q
        inLeft = self.containsPq(root.left, p, q)

        # if right subtree contains p or q
        inRight = self.containsPq(root.right, p, q)

        # cases for root to be LCA, will never trigger for non LCA node above,
        # since only one condition can be true then (both either in left or right),
        # so lca will never update twice
        if (isRoot and inLeft) or (isRoot and inRight) or (inLeft and inRight):
            self.lca = root

        # return indication whether current subtree contains p or q
        # so above node can check if it is LCA
        return isRoot or inLeft or inRight
