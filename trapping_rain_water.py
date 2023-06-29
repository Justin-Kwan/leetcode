class Solution:
    # one map bottom up dp approach
    def trap(self, heights: List[int]) -> int:
        # no water can be trapped with 2 or less blocks
        if len(heights) <= 2:
            return 0

        rightCache = [0] * len(heights)
        trappedWaterCount = 0

        # only build single map of max block heights to right of each block
        for i in range(len(heights) - 2, -1, -1):
            maxRightHeight = max(heights[i + 1], rightCache[i + 1])
            rightCache[i] = maxRightHeight

        # carry over max block height to left of each block without storing,
        # then compute water trapped at current block
        maxLeftHeight = 0
        for i in range(1, len(heights)):
            maxLeftHeight = max(heights[i - 1], maxLeftHeight)
            # since water height at current block calculated from ground level,
            # subtract height of current block to account for overflowing
            curWaterCount = min(maxLeftHeight, rightCache[i]) - heights[i]
            trappedWaterCount += max(0, curWaterCount)

        return trappedWaterCount

    # # two map bottom up dp approach
    # def trap(self, heights: List[int]) -> int:
    #     # no water can be trapped with 2 or less blocks
    #     if len(heights) <= 2:
    #         return 0

    #     leftCache, rightCache = [0] * len(heights), [0] * len(heights)
    #     trappedWaterCount = 0

    #     leftPos, rightPos = 1, len(heights) - 2
    #     while rightPos >= 0 and leftPos < len(heights):
    #         # carry over max block height to left and right of current block
    #         maxLeftHeight = max(heights[leftPos - 1], leftCache[leftPos - 1])
    #         maxRightHeight = max(heights[rightPos + 1], rightCache[rightPos + 1])

    #         # save max block height to left and right of current block
    #         leftCache[leftPos], rightCache[rightPos] = maxLeftHeight, maxRightHeight
    #         leftPos += 1
    #         rightPos -= 1

    #     for i in range(len(heights)):
    #         # since water height at current block calculated from ground level,
    #         # subtract height of current block to account for overflowing
    #         curWaterCount = min(leftCache[i], rightCache[i]) - heights[i]
    #         trappedWaterCount += max(0, curWaterCount)

    #     return trappedWaterCount

    # # top down dp approach
    # def trap(self, heights: List[int]) -> int:
    #     leftCache, rightCache = {}, {}
    #     trappedWaterCount = 0

    #     for i in range(len(heights)):
    #         # search for max block height to left and right of current block
    #         maxLeftHeight = self.searchMaxNeighbor(heights, i, leftCache, "left")
    #         maxRightHeight = self.searchMaxNeighbor(heights, i, rightCache, "right")

    #         # since water height at current block calculated from ground level,
    #         # subtract height of current block to account for overflowing
    #         curWaterCount = min(maxLeftHeight, maxRightHeight) - heights[i]
    #         trappedWaterCount += max(0, curWaterCount)

    #     return trappedWaterCount

    # def searchMaxNeighbor(self, heights: List[int], i: int, cache: Dict[int, int], direction: str) -> int:
    #     # stop searching once reached left or right ends of map
    #     if (direction == "left" and i <= 0) or (direction == "right" and i >= len(heights) - 1):
    #         return 0
    #     if i in cache:
    #         return cache[i]

    #     nextPos = i - 1 if direction == "left" else i + 1
    #     maxHeightUpto = max(heights[nextPos], self.searchMaxNeighbor(heights, nextPos, cache, direction))

    #     # cache the max left/right block height at current position
    #     cache[i] = maxHeightUpto
    #     return maxHeightUpto
