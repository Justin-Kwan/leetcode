class Solution:
    # test cases:
    # input: [1] target = 1
    # left = 0, right = 0, middle = 0
    # output: 0
    #
    # input: [1] target = 2
    # left = 1, right = 0, middle = 0
    # output: -1
    #
    # input: [1, 2, 3, 4, 5] target = 4
    # left = 3, right = 4, middle = 3
    # output: 3
    #
    # input: [3, 4, 5, 1, 2] target = 1
    # left = 3, right = 3, middle = 3
    # pivot = 3
    # output: 3
    #
    # input: [2, 3, 4, 5, 1] target = 1
    # left = 4, right = 4, middle = 4
    # pivot = 4
    # output: 4
    #
    # input: [1, 0] target = 1
    # left = 1, right = 1, middle = 0
    # pivot = 1
    # output: 0
    #
    # search pivot then target approach
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # search for first pivot index in array
        #
        # left will reach pivot and right will cross over, or left crosses over
        # right at end if not rotated (pivot is after last index)
        while left <= right:
            middle = (left + right) // 2
            # in left unrotated region, move left pointer closer to pivot
            if nums[middle] >= nums[0]:
                left = middle + 1
            # in right rotated region, move right pointer closer to pivot
            else:
                right = middle - 1

        # search for target number within it's region
        if target >= nums[0]:
            # search target in non-rotated region or entire array if not rotated
            return self.binarySearch(nums, 0, left - 1, target)
        else:
            # search target in rotated region
            return self.binarySearch(nums, left, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
