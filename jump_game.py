class Solution:
#     # optimized (memoized) top down dp
#     def canJump(self, maxJumpLengths: List[int]) -> bool:
#         if len(maxJumpLengths) == 1:
#             return True

#         return self.canReachLastElement(0, maxJumpLengths, set())

#     def canReachLastElement(self, fromIndex: int, maxJumpLengths: List[int], unreachableFromIndexes: set[int]):
#         # when passed in index is out of range or
#         # when end is not reachable from cache (already computed)
#         if fromIndex >= len(maxJumpLengths) or fromIndex in unreachableFromIndexes:
#             return False

#         # when last index is reached
#         if fromIndex == len(maxJumpLengths) - 1:
#             return True

#         # reverse iterate to catch cases where largest jump can reach end faster (stretch to reach end first)
#         for jumpLength in range(maxJumpLengths[fromIndex], 0, -1):
#             if self.canReachLastElement(fromIndex + jumpLength, maxJumpLengths, unreachableFromIndexes):
#                 return True

#         unreachableFromIndexes.add(fromIndex)
#         return False

    # optimized greedy
    def canJump(self, maxJumpLengths: List[int]) -> bool:
        if not maxJumpLengths:
            return True

        endIndex = len(maxJumpLengths) - 1
        currIndexReachingEnd = endIndex

        for i in range(endIndex, -1, -1):
            maxJumpIndex = i + maxJumpLengths[i]

            # if ith index can jump to current index that can reach end,
            # then ith index can reach end
            if currIndexReachingEnd <= maxJumpIndex:
                currIndexReachingEnd = i

        return True if currIndexReachingEnd == 0 else False
