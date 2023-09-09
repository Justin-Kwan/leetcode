class Solution:
    # test cases:
    # L   M   R
    #  M
    #  L  R
    #     L
    # [1, 2, 3, 4, 5] target = 2
    #
    # R L  
    #  [1, 2] target = 0
    #
    #     R L
    # [1, 2] target = 3
    #
    # R L
    #   [] target = 1
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
