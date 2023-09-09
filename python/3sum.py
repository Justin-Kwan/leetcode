class Solution:
    # optimal sorted and two pointers approach
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletSummands = []

        # sort to detect and skip modulating duplicate values at current anchor
        nums.sort()

        # assume each value as first anchor (number to modulate on)
        for i in range(0, len(nums)):
            # avoid remodulating on number already seen (prevent duplicates of same order)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            zeroComplement = -nums[i]

            # find two numbers (anchors) that sum to zero complement of first anchor
            self.twoSum(zeroComplement, i, nums, tripletSummands)

        return tripletSummands

    def twoSum(self, target: int, firstPos: int, nums: List[int], tripletSummands: List[List[int]]) -> None:
        # second anchor always begins modulating after first to prevent duplicates of
        # different order
        leftPos = firstPos + 1
        rightPos = len(nums) - 1

        # modulate second and third anchors to find summand pair
        while leftPos < rightPos:
            # avoid remodulating on second number already seen
            # (prevent duplicates of same order)
            if leftPos > firstPos + 1 and nums[leftPos] == nums[leftPos - 1]:
                leftPos += 1
                continue

            pairSum = nums[leftPos] + nums[rightPos]

            if pairSum < target:
                leftPos += 1
            elif pairSum > target:
                rightPos -= 1
            else:
                tripletSummands.append([nums[firstPos], nums[leftPos], nums[rightPos]])
                # both anchors must be shifted, since no other value exists on either side
                # for both to yield target sum (continue modulating)
                leftPos += 1
                rightPos -= 1

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
