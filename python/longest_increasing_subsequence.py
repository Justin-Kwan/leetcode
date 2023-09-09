class Solution:
#     # optimized top down dp memoized
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         maxLIS = 0
#         cache = {}

#         for i in range(len(nums)):
#             maxLIS = max(self.findMaxLIS(i, nums, cache), maxLIS)

#         return maxLIS

#     def findMaxLIS(self, curPos: int, nums: List[int], cache: Dict[int, int]) -> int:
#         # once last number is reached
#         if curPos == len(nums) - 1:
#             return 1

#         # if LIS at current number (position) is memoized
#         if curPos in cache:
#             return cache[curPos]

#         maxLIS = 0

#         # max increasing subsequence length starting at current number is
#         # max across all larger numbers
#         for i in range(curPos + 1, len(nums)):
#             if nums[i] > nums[curPos]:
#                 maxLIS = max(self.findMaxLIS(i, nums, cache), maxLIS)

#         # memoize LIS for current number (position) to avoid future recomputations
#         cache[curPos] = maxLIS + 1
#         return cache[curPos]

    # unoptimized bottom up dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxLISByPos = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # find the max increasing subsequence length across all numbers larger
            # than current to the right
            maxLISAhead = 0

            # take max of increasing subsequence lengths for all larger numbers
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maxLISAhead = max(maxLISByPos[j], maxLISAhead)

            maxLISByPos[i] += maxLISAhead

        return max(maxLISByPos)
