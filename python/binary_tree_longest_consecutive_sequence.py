# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def longestConsecutive(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return self.findLongestConsecutive(root)["global"]

#     # simplified bottom up dfs, thread safe
#     def findLongestConsecutive(self, root: Optional[TreeNode]) -> Dict[int, int]:
#         # no consecutive nodes exist in subtree of null
#         if not root: 
#             return {"local": 0, "global": 0}
        
#         # reuse lengthFromLeft to store max length at current node to save memory
#         lengthFromLeft = self.findLongestConsecutive(root.left)
#         lengthFromRight = self.findLongestConsecutive(root.right)

#         # assume L/R are part of path to current node, increment for now
#         lengthFromLeft["local"] += 1
#         lengthFromRight["local"] += 1

#         # left does not continue current node's path, reset current length
#         if root.left and root.left.val != root.val + 1:
#             lengthFromLeft["local"] = 1
#         # right does not continue current node's path, reset current length
#         if root.right and root.right.val != root.val + 1:
#             lengthFromRight["local"] = 1

#         # take max between L/R local paths
#         lengthFromLeft["local"] = max(lengthFromLeft["local"], lengthFromRight["local"])
#         # take max between L/R local and L/R global paths
#         lengthFromLeft["global"] = max(lengthFromLeft["local"], lengthFromLeft["global"], lengthFromRight["global"])

#         return lengthFromLeft 

#     # bottom up dfs, thread safe
#     def findLongestConsecutive(self, root: Optional[TreeNode]) -> Dict[int, int]:
#         # no consecutive nodes exist in subtree of null
#         if not root:
#             return {"local": 0, "global": 0}

#         # reuse lengthFromLeft to store max length at current node to save memory
#         lengthFromLeft = self.findLongestConsecutive(root.left)
#         lengthFromRight = self.findLongestConsecutive(root.right)

#         isSequenceInLeft = root.left and root.left.val == root.val + 1
#         isSequenceInRight = root.right and root.right.val == root.val + 1

#         # both left and right continue the path, take max local path length
#         if isSequenceInLeft and isSequenceInRight:
#             lengthFromLeft["local"] = max(lengthFromLeft["local"], lengthFromRight["local"]) + 1
#         # only left continues the path, update local path length
#         elif isSequenceInLeft:
#             lengthFromLeft["local"] += 1
#         # only right continues the path, update local path length
#         elif isSequenceInRight:
#             lengthFromLeft["local"] = lengthFromRight["local"] + 1
#         # no child continues the path, reset local path length
#         else:
#             lengthFromLeft["local"] = 1

#         # take max between L/R local and L/R global paths
#         lengthFromLeft["global"] = max(lengthFromLeft["local"], lengthFromLeft["global"], lengthFromRight["global"])

#         return lengthFromLeft

#     # simplified bottom up dfs, non thread safe
#     maxConsecutiveLength = 0
#     def longestConsecutive(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         self.findLongestConsecutive(root)
#         return self.maxConsecutiveLength

#     def findLongestConsecutive(self, root: Optional[TreeNode]) -> Dict[int, int]:
#         if not root:
#             return 0

#         # get local length at current node, assume it continues from L/R children
#         lengthFromLeft = self.findLongestConsecutive(root.left) + 1
#         lengthFromRight = self.findLongestConsecutive(root.right) + 1

#         # left does not continue from current node path, reset length
#         if root.left and root.val + 1 != root.left.val:
#             lengthFromLeft = 1
#         # right does not continue from current node path, reset length
#         if root.right and root.val + 1 != root.right.val:
#             lengthFromRight = 1

#         # take max between local L/R path lengths
#         maxLocalLength = max(lengthFromLeft, lengthFromRight)
#         # update global max path length with existing or new local legnth
#         self.maxConsecutiveLength = max(maxLocalLength, self.maxConsecutiveLength)

#         return maxLocalLength

    # optimized preorder dfs with accumulator
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.findLongestConsecutive(root, root.val - 1, 0, 0)

    def findLongestConsecutive(self, root: Optional[TreeNode], parentVal: int, curLength: int, maxLength: int) -> int:
        # return max consecutive length seen on current branch
        if not root:
            return maxLength

        # increment current length if current node continues from parent
        if parentVal + 1 == root.val:
            curLength += 1
        else:
            curLength = 1

        # update max consecutive length seen so far from root to current node
        maxLength = max(curLength, maxLength)

        return max(self.findLongestConsecutive(root.left, root.val, curLength, maxLength), self.findLongestConsecutive(root.right, root.val, curLength, maxLength))
