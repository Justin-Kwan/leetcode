class Solution:
    #    l
    #    r
    # [1,8,6,2,5,4,8,3,7]
    # maxWaterArea = 49
    # currWaterArea = 49
    #
    #          l     r
    # [2,3,4,5,18,17,6]
    # maxWaterArea = 16
    # currWaterArea = 12
    # optimal two pointers (greedy)
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWaterArea = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            # update global max water area so far
            maxWaterArea = max(maxWaterArea, height * width)

            # pointer with shorter height should find higher one
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWaterArea
