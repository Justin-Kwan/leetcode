class Solution:
    # test cases:
    #                                i
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # maxSum = 6
    # maxSumAtCur = -2, 1, -2, 4, 3, 5, 6, 1, 5
    # maxSumAtPrev = 5
    #
    #                   i
    # [-4, -31, -30, -1]
    # maxSum = -1
    # maxSumAtCur = -4, -31, -30, -1
    # maxSumAtPrev = -1
    #
    #          i
    # [0, 0, 0]
    # maxSum = 0
    # maxSumAtCur = 0
    # maxSumAtPrev = 0
    #
    # []
    # maxSum = 0
    #
    #    i
    # [1]
    # maxSum = 1
    # maxSumAtCur = 1
    # maxSumAtPrev = 1
    #
    # optimal bottom up dp approach
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # track global max subarray sum, compare against each local
        # sum of max subarray ending at each number
        maxSum, maxSumAtCur = float('-inf'), 0

        for num in nums:
            # sum of max subarray ending at current number is either
            # current number + sum of max subarray ending at previous
            # or current number itself whichever larger
            maxSumAtCur = max(maxSumAtCur + num, num)
            maxSum = max(maxSumAtCur, maxSum)

        return maxSum
