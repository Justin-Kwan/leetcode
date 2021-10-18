class Solution:
#     # optimized top down dp memoized
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numsByConsecutiveCount = {}
#         maxConsecutiveCount = 0

#         # build cached numbers by initial count, treat duplicates as same
#         for num in nums:
#             numsByConsecutiveCount[num] = -1

#         # find max consecutive increasing sequence
#         for num in nums:
#             currConsecutiveCount = self.countLongestConsecutive(num, numsByConsecutiveCount)
#             maxConsecutiveCount = max(currConsecutiveCount, maxConsecutiveCount)

#         return maxConsecutiveCount

#     def countLongestConsecutive(self, num: int, numsByConsecutiveCount: dict[int, int]) -> int:
#         # number is not in cache, so sequence ends
#         if num not in numsByConsecutiveCount:
#             return 0

#         # number's sequence count is fresh (already visited yet)
#         if numsByConsecutiveCount[num] != -1:
#             return numsByConsecutiveCount[num]

#         # number not yet visited in any sequence
#         # current sequence count depends on next number's sequence count
#         currConsecutiveCount = self.countLongestConsecutive(num + 1, numsByConsecutiveCount) + 1

#         # write to cache
#         numsByConsecutiveCount[num] = currConsecutiveCount

#         return currConsecutiveCount

    # optimized iterative
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxConsecutiveCount = 0

        # find max consecutive increase sequence count by counting
        # sequence values in contiguous blocks
        for num in nums:
            if num - 1 in numbers:
                continue

            # current number starts new sequence since previous not in list (gap)

            currConsecutiveCount = 1

            # keep checking next sequence value so long as it exists
            while num + currConsecutiveCount in numbers:
                currConsecutiveCount += 1

            maxConsecutiveCount = max(currConsecutiveCount, maxConsecutiveCount)

        return maxConsecutiveCount
