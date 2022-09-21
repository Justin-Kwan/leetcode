class Solution:
    # optimal
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
 
        # first element could be max sum subarray,
        # will be replaced on next iteration if not
        maxSumSoFar = nums[0]
        maxSumAtCurr = nums[0]

        for i in range(1, len(nums)):
            # update local max sum up to current
            # (previous max sum + current or current itself)
            maxSumAtCurr = max(nums[i] + maxSumAtCurr, nums[i])
            # update global max sum
            maxSumSoFar = max(maxSumSoFar, maxSumAtCurr)

        return maxSumSoFar
