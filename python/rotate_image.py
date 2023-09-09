class Solution:
    # optimized reflect then transpose
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.reflectRows(matrix)
        self.reflectValuesDiagonally(matrix)

    def reflectRows(self, matrix: List[List[int]]) -> None:
        matrixLength = len(matrix)

        for rowPos in range(matrixLength // 2):
            for colPos in range (matrixLength):
                tempValue = matrix[rowPos][colPos]
                matrix[rowPos][colPos] = matrix[matrixLength - 1 - rowPos][colPos]
                matrix[matrixLength - 1 - rowPos][colPos] = tempValue

    # transpose matrix (about diagonal axis)
    def reflectValuesDiagonally(self, matrix: List[List[int]]) -> None:
        matrixLength = len(matrix)

        for rowPos in range(matrixLength):
            # only flip values at and above axis to avoid double flipping
            for colPos in range(rowPos, matrixLength):
                tempValue = matrix[rowPos][colPos]
                matrix[rowPos][colPos] = matrix[colPos][rowPos]
                matrix[colPos][rowPos] = tempValue
