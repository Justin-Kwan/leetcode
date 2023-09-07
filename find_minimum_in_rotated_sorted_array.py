class Solution:
    # right cross left pointer approach
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        # binary search until smallest pivot element found once left
        # pointer reached it and right pointer crosses left
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # middle in left un-rotated side so move it closer to pivot
            if nums[middle] >= nums[0]:
                left = middle + 1
            # middle in right rotated side so move it closer to pivot
            else:
                right = middle - 1

        # left pointer will have exhausted past last index if not rotated
        return nums[left] if left < len(nums) else nums[0]

    # # left reach right pointer approach
    # def findMin(self, nums: List[int]) -> int:
    #     if not nums:
    #         return -1

    #     # minimum is first if not rotated
    #     if nums[0] < nums[-1]:
    #         return nums[0]

    #     # binary search until smallest pivot element found once left
    #     # and right pointers both reach it
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         middle = (left + right) // 2
    #         # middle in left un-rotated side so move it closer to pivot
    #         if nums[middle] >= nums[0]:
    #             left = middle + 1
    #         # middle in right rotated side so move it closer to pivot
    #         else:
    #             right = middle

    #     return nums[left]
