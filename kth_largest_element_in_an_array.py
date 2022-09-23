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

    # min heap non-modifying
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        # use min heap to easily eject numbers below k that we don't care about,
        # to optimize average case space complexity when k < len(nums)
        kLargestNums = []

        for num in nums:
            heapq.heappush(kLargestNums, num)

            # if length becomes k+1, remove root which is definitely below kth largest
            if len(kLargestNums) > k:
                heapq.heappop(kLargestNums)

        # kthlargest number sits at root of heap, pushed up by larger numbers
        return kLargestNums[0]
