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
    # optimal greedy two pointers approach
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")
        leftPos, rightPos = 0, len(heights) - 1

        # search for two heights yielding max height
        while leftPos < rightPos:
            # current area is bounded by shortest height
            curArea = (rightPos - leftPos) * min(heights[leftPos], heights[rightPos])
            maxArea = max(curArea, maxArea)

            # pointer with shorter height should find higher one
            #
            # as a contradiction, since shifting the higher height will definitely not
            # yield a larger area because the area is limited by the shorter height
            if heights[leftPos] < heights[rightPos]:
                leftPos += 1
            else:
                rightPos -= 1

        return maxArea
