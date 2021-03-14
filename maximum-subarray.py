class Solution:
    # optimal
    def maxSubArray(self, nums: List[int]) -> int:
        # first element could be max sum subarray
        # will be replaced on next iteration if not
        maxSumSoFar = nums[0]
        currMaxSum = nums[0]

        for i in range(1, len(nums)):
            currMaxSum = max(currMaxSum + nums[i], nums[i])

            if currMaxSum > maxSumSoFar:
                maxSumSoFar = currMaxSum
                
        return maxSumSoFar
