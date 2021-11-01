class Solution:
    # optimized bottom up DP
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxSumUpToPrevPrev = nums[0]
        maxSumUpToPrev = max(maxSumUpToPrevPrev, nums[1])
        maxSumUpToCurr = maxSumUpToPrev         # handle list of length 2 case

        for house in range(2, len(nums)):       # start at third house
            # either can add to sequence i - 2 away to make larger, or point to larger i - 1 sequence sum (as local max)
            maxSumUpToCurr = max(maxSumUpToPrev, maxSumUpToPrevPrev + nums[house])
            maxSumUpToPrevPrev = maxSumUpToPrev
            maxSumUpToPrev = maxSumUpToCurr

        return maxSumUpToCurr

#     # brute force bottom up dp
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         # must keep previous sum up to ouse since cannot rely on prev or prev - 1
#         maxSumUpToHouse = [0 for i in range(len(nums))]

#         for house in range(0, len(nums)):
#             # take max of prev sublist's non-adjacent array sum
#             for prevHouse in range(0, house - 1):
#                 maxSumUpToHouse[house] = max(maxSumUpToHouse[house], maxSumUpToHouse[prevHouse])

#             maxSumUpToHouse[house] += nums[house]

#         return max(maxSumUpToHouse)


#     # optimized dfs with memoization (top down dp)
#     def rob(self, houses: List[int]) -> int:
#         if not houses:
#             return 0
#         if len(houses) == 1:
#             return houses[0]

#         maxSumAtHouse = {}

#         # can reach every element (and rob combo) from first and second
#         return max(
#             self.findMaxNonAdjacentSum(0, houses, maxSumAtHouse),
#             self.findMaxNonAdjacentSum(1, houses, maxSumAtHouse))

#     def findMaxNonAdjacentSum(self, house: int, houses: List[int], maxSumAtHouse: dict[int, int]) -> int:
#         # next non-adjacent house does not exist
#         if house + 2 >= len(houses):
#             return houses[house]

#         # hit cache for max non-adjacent sum path from house
#         if house in maxSumAtHouse:
#             return maxSumAtHouse[house]

#         maxRobbedHouseSum = 0

#         # if max non-adjacent subarray sum not in cache for house,
#         # compute it from current by finding max paths of all non-adjacent
#         # nums after current house
#         for i in range(house + 2, len(houses)):
#             robbedHouseSum = houses[house] + self.findMaxNonAdjacentSum(i, houses, maxSumAtHouse)
#             maxRobbedHouseSum = max(maxRobbedHouseSum, robbedHouseSum)

#         maxSumAtHouse[house] = maxRobbedHouseSum
#         return maxRobbedHouseSum
