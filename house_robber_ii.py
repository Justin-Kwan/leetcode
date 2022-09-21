class Solution:
    # optimal bottom up dfs, multiple rotated passes approach
    def rob(self, nums: List[int]) -> int:
        # assume single house on cyclic street is not neighbor of itself
        if len(nums) == 1:
            return nums[0]

        # max robbable sum cannot include both head and tail, take max between unique combinations
        return max(self.findMaxNonAdjacentSum(nums, 0, len(nums) - 2), self.findMaxNonAdjacentSum(nums, 1, len(nums) - 1))

    def findMaxNonAdjacentSum(self, nums: List[int], start: int, end: int) -> int:
        if start < 0 or start >= len(nums) or end < 0 or end >= len(nums):
            return 0

        # last number has no max at previous positions
        maxSumAtCur, maxSumAtPrev, maxSumAtPrevPrev = nums[len(nums) - 1], 0, 0

        # build up max non-adjacent sums from each position
        while start <= end:
            maxSumAtCur = max(maxSumAtPrev, nums[end] + maxSumAtPrevPrev)
            # update max sum from previous positions, shifting them to next left number
            maxSumAtPrevPrev = maxSumAtPrev
            maxSumAtPrev = maxSumAtCur
            end -= 1

        return maxSumAtCur
