import random

class Solution:
#     # max heap modifying
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) == 0:
#             return 0

#         heapq._heapify_max(nums)

#         # continue popping max value until kth largest is retrieved
#         curMax = float('-inf')
#         while k >= 1:
#             curMax = heapq._heappop_max(nums)
#             k -= 1

#         return curMax

#     # min heap non-modifying
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if len(nums) == 0:
#             return 0

#         # use min heap to easily eject numbers below k that we don't care about,
#         # to optimize average case space complexity when k < len(nums)
#         kLargestNums = []

#         for num in nums:
#             heapq.heappush(kLargestNums, num)

#             # if length becomes k+1, remove root which is definitely below kth largest
#             if len(kLargestNums) > k:
#                 heapq.heappop(kLargestNums)

#         # kthlargest number sits at root of heap, pushed up by larger numbers
#         return kLargestNums[0]

    # optimal quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        return self.quickSelect(nums, k, 0, len(nums) - 1)

    def quickSelect(self, nums: List[int], k: int, start: int, end: int) -> int:
        # finally reached kth largest number
        if start == end:
            return nums[start]

        # pick random pivot to partition numbers around
        pivotPos = random.randint(start, end)
        sortedPivotPos = self.partition(nums, pivotPos, start, end)

        # pivot number is kth largest, found early
        if sortedPivotPos == len(nums) - k:
            return nums[sortedPivotPos]
        # kth largest in left smaller group
        elif sortedPivotPos > len(nums) - k:
            return self.quickSelect(nums, k, start, sortedPivotPos - 1)
        # kth largest in right larger group
        else:
            return self.quickSelect(nums, k, sortedPivotPos + 1, end)

    # given a position of a number to pivot around, return its position in sorted order.
    def partition(self, nums: List[int], pivotPos: int, start: int, end: int) -> int:
        # temporarily move pivot number out of the way
        nums[pivotPos], nums[end] = nums[end], nums[pivotPos]

        nextSmallerPos = start
        for i in range(start, end):
            # throw ith number (smaller than pivot) to end of smaller group
            if nums[i] <= nums[end]:
                nums[nextSmallerPos], nums[i] = nums[i], nums[nextSmallerPos]
                nextSmallerPos += 1

        # put pivot number back right after smaller group
        nums[end], nums[nextSmallerPos] = nums[nextSmallerPos], nums[end]
        return nextSmallerPos
