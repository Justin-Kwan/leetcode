class Solution:
    # optimal binary search approach
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        # treat 2d array as 1d array while searching
        numRows, numCols = len(matrix), len(matrix[0])
        leftPos, rightPos = 0, (numRows * numCols) - 1

        while leftPos <= rightPos:
            middlePos = (leftPos + rightPos) // 2
            # count number of rows that fit up to index and leftover columns
            middleValue = matrix[middlePos // numCols][middlePos % numCols]

            # target value found early at middle position
            if middleValue == target:
                return True
            elif middleValue < target:
                leftPos = middlePos + 1
            else:
                rightPos = middlePos - 1

        # left and right pointers crossed so target not in matrix
        return False
