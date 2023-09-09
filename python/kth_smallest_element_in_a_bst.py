# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # optimized iterative in-order traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        parentNodes = []
        # last popped node
        parentNode = None

        while True:
            # reached kth in order node
            if k == 0:
                break
            # visit current after visiting left subtree
            if root:
                parentNodes.append(root)
                root = root.left
            # base case, return to parent node and then visit right
            else:
                parentNode = parentNodes.pop()
                k -= 1
                root = parentNode.right

        return parentNode.val
