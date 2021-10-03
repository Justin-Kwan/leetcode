class Solution:
    # optimized bottom up DP
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxSumUpToPrevPrev = nums[0]
        maxSumUpToPrev = max(nums[0], nums[1])
        maxRobbableSum = maxSumUpToPrev         # handle list of length 2 case

        for house in range(2, len(nums)):
            # either can add to sequence i - 2 away to make larger, or point to larger i - 1 sequence sum (as local max)
            maxSumUpToCurr = max(maxSumUpToPrevPrev + nums[house], maxSumUpToPrev)
            maxSumUpToPrevPrev = maxSumUpToPrev
            maxSumUpToPrev = maxSumUpToCurr

            # update global non-adjacent max subarray sum
            maxRobbableSum = max(maxSumUpToCurr, maxRobbableSum)

        return maxRobbableSum

#     # bottom up DP
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


#     # optimized DFS with memoization (top down DP)
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         maxRobbableSum = 0
#         maxSumUpToHouse = [-1 for i in range(len(nums))]

#         for house in range(0, len(nums)):
#             maxRobbableSum = max(
#                 maxRobbableSum,
#                 self.searchMaxRobbableSum(house, nums, maxSumUpToHouse))

#         return maxRobbableSum

#     def searchMaxRobbableSum(self, house: int, nums: List[int], maxSumUpToHouse: List[int]) -> int:
#         if house >= len(nums):
#             return 0
#         if maxSumUpToHouse[house] != -1:
#             return maxSumUpToHouse[house]

#         maxRobbableSum = 0

#         # if max non-adjacent subarray sum not in cache for house, compute it
#         for nextHouse in range(house + 2, len(nums)):
#             maxRobbableSum = max(
#                 maxRobbableSum,
#                 self.searchMaxRobbableSum(nextHouse, nums, maxSumUpToHouse))
            
#         maxRobbableSum += nums[house]
            
#         # store in cache
#         maxSumUpToHouse[house] = maxRobbableSum
#         return maxRobbableSum
