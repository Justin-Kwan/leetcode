class Solution:
    # suboptimal hashset approach
    def firstMissingPositive(self, nums: List[int]) -> int:
        seenNums = set(nums)

        # find first positive number in sequence than could fit within
        # length of list but does not exist since pushed out
        for num in range(1, len(nums) + 1):
            if num not in seenNums:
                return num

        # next number in continuing sequence that starts from 1
        return len(nums) + 1
