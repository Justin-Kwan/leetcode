class Solution:
    # optimized sorted and two pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numCount = len(nums)
        summandTriplets = []

        nums.sort()

        for i in range(0, numCount):
            # skip same contiguous fixed numbers (to prevent duplicate triplets since searching forwards)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # search all triplets starting from ith index
            self.findSummandTriplets(i, nums, summandTriplets)

        return summandTriplets
    
    def findSummandTriplets(self, i: int, nums: List[int], summandTriplets: List[List[int]]):
        lowPtr = i + 1
        highPtr = len(nums) - 1

        while lowPtr < highPtr:
            # only skip when nums[lowPtr] = nums[lowPtr - 1] after lowPtr has actually
            # independenty moved up, not when lowPtr moves up with i
            if nums[lowPtr] == nums[lowPtr - 1] and lowPtr - 1 != i:
                lowPtr += 1
                continue

            currSum = nums[i] + nums[lowPtr] + nums[highPtr]

            if currSum == 0:
                summandTriplets.append([nums[i], nums[lowPtr], nums[highPtr]])
                lowPtr += 1
                highPtr -= 1
            elif currSum < 0:
                lowPtr += 1     # move up low pointer to increase sum
            else:
                highPtr -= 1    # move down high pointer to decrease sum

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         numsByIndex = {}
#         numsCount = len(nums)
#         summandTriplets = set()

#         nums.sort()

#         # dump nums and count into map
#         for i in range(0, numsCount):
#             numsByIndex[nums[i]] = i

#         # for each number
#         for i in range(0, numsCount):
#             # when positive number is reached, it cannot sum with any subsequent positive numbers to 0 (since sorted),
#             # all subsequent numbers would have already been added in triplets in previous negative numbers, or be part
#             # of no triplets (since a positive must take at least 1 negative to get 0)
#             if nums[i] >= 1:
#                 break

#             target = (-nums[i])

#             # skip duplicate value since we only keep unique triplets
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             # find all pairs that sum to -number
#             for j in range(0, numsCount):
#                 # do not skip here since i and i + 1 could both be in the same triplet even if equal
#                 if i == j:
#                     continue

#                 complement = target - nums[j]
#                 summandTriplet = tuple(sorted((nums[i], nums[j], complement)))

#                 if complement in numsByIndex and numsByIndex[complement] != i and numsByIndex[complement] != j and summandTriplet not in summandTriplets:
#                     summandTriplets.add(summandTriplet)

#         return summandTriplets
