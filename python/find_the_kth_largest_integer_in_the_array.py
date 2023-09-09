class Solution:
#     # heapify approach
#     def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         for i in range(len(nums)):
#             nums[i] = int(nums[i])

#         heapq._heapify_max(nums)

#         while k >= 1:
#             num = heapq._heappop_max(nums)
#             k -= 1

#         return str(num)

    # non modifying heap approach
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        kLargestNums = []

        for num in nums:
            heapq.heappush(kLargestNums, int(num))

            # eject number definitely below kth largest number
            if len(kLargestNums) > k:
                heapq.heappop(kLargestNums)

        # kth largest number should sit at top of min heap of size k
        return str(kLargestNums[0])
