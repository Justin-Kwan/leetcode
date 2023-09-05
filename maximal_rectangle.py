class Solution:
    # optimal bottom up dp approach
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        maxHeights = [0] * len(matrix[0])
        minLeftBounds = [float('-inf')] * len(matrix[0])
        maxRightBounds = [float('inf')] * len(matrix[0])

        for row in range(len(matrix)):
            # compute max heights from each cell using previous row's max heights
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    maxHeights[col] += 1
                else:
                    maxHeights[col] = 0

            minLeftBound, maxRightBound = 0, len(matrix[row]) - 1
            # compute minimum left bound of rectangle that maximizes height from each cell
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    # current cell's rectangle left bound is either previous one above with
                    # tighter bound that maximizes height, or current left bound of first
                    # '1' cell seen if no tigher bound from above exists
                    minLeftBounds[col] = max(minLeftBound, minLeftBounds[col])
                else:
                    minLeftBounds[col] = float('-inf')
                    minLeftBound = col + 1

            # compute maximum right bound of rectangle that maximizes height from each cell
            for col in range(len(matrix[row]) - 1, -1, -1):
                if matrix[row][col] == '1':
                    # current cell's rectangle right bound is either previous one above with
                    # tighter bound that maximizes height, or current right bound of first
                    # '1' cell seen if no tigher bound from above exists
                    maxRightBounds[col] = min(maxRightBound, maxRightBounds[col])
                else:
                    maxRightBounds[col] = float('inf')
                    maxRightBound = col - 1

            # compute max rectangle area given max height and min left and max right rectangle
            # bounds from each cell
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    curArea = maxHeights[col] * (maxRightBounds[col] - minLeftBounds[col] + 1)
                    maxArea = max(curArea, maxArea)

        return maxArea
