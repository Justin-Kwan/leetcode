class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowCount, colCount = len(matrix), len(matrix[0])   
        maxUpperRow, maxLowerRow = 0, rowCount - 1
        maxLeftCol, maxRightCol = 0, colCount - 1

        elementsInSpiralOrder = []

        while len(elementsInSpiralOrder) < rowCount * colCount:
            # move left to right on top
            for col in range(maxLeftCol, maxRightCol + 1):
                elementsInSpiralOrder.append(matrix[maxUpperRow][col])

            # move top to bottom on right (skip top right)
            for row in range(maxUpperRow + 1, maxLowerRow + 1):
                elementsInSpiralOrder.append(matrix[row][maxRightCol])

            # move right to left on bottom (skip if already done when matrix is single row)
            if maxUpperRow != maxLowerRow:
                # skip bottom right
                for col in range(maxRightCol - 1, maxLeftCol - 1, -1):
                    elementsInSpiralOrder.append(matrix[maxLowerRow][col])

            # move bottom to top on left (skip if already done when matrix is single column)
            if maxLeftCol != maxRightCol:
                # skip bottom left, skip top left
                for row in range(maxLowerRow - 1, maxUpperRow, -1):
                    elementsInSpiralOrder.append(matrix[row][maxLeftCol])
                    
            # shift in bounds on all sides
            maxUpperRow += 1
            maxLowerRow -= 1
            maxLeftCol += 1
            maxRightCol -= 1

        return elementsInSpiralOrder            
