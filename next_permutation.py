class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first decreasing number before sequence of maximized value (exhausted)
        firstDecreasingPos = len(nums) - 2
        while firstDecreasingPos >= 0 and nums[firstDecreasingPos] >= nums[firstDecreasingPos + 1]:
            firstDecreasingPos -= 1

        # if all digits are descending or equal permutation already maximizes value, so reset to first (smallest), edge case
        if firstDecreasingPos < 0:
            self.reverseNums(nums, 0, len(nums) - 1)
            return

        # find next largest value in decreasing sequence (remaining decision space) to replace first decreasing digit
        nextLargestPos = len(nums) - 1
        while firstDecreasingPos < nextLargestPos and nums[firstDecreasingPos] >= nums[nextLargestPos]:
            nextLargestPos -= 1

        # replace first decrasing value with next largest option to permute
        nums[firstDecreasingPos], nums[nextLargestPos] = nums[nextLargestPos], nums[firstDecreasingPos]
        self.reverseNums(nums, firstDecreasingPos + 1, len(nums) - 1)

    def reverseNums(self, nums: List[int], start: int, end: int) -> None:
        if (start < 0 or start >= len(nums)) or (end < 0 or end >= len(nums)):
            return

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
