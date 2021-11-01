class Solution:
    # optimized greedy/bottom up dp
    def canJump(self, nums: List[int]) -> bool:
        linkToEnd = len(nums) - 1

        # can each previous element reach latest link to end
        for i in range(len(nums) - 1, -1, -1):
            # if (previous index + jump count) can reach linkToEnd
            if i + nums[i] >= linkToEnd:
                linkToEnd = i

        return linkToEnd == 0


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
