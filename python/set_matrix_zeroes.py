class Solution:
#     # non optimal
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         for row in range(len(matrix)):
#             for col in range(len(matrix[row])):
#                 if matrix[row][col] == 0:
#                     self.setRowToZero(matrix[row])
#                     self.setColToZero(matrix, col)
#         for row in range(len(matrix)):
#             for col in range(len(matrix[row])):
#                 if matrix[row][col] == float("inf"):
#                     matrix[row][col] = 0
    
#     def setRowToZero(self, matrixRow: List[int]):
#         for col in range(len(matrixRow)):
#             if matrixRow[col] != 0:
#                 matrixRow[col] = float("inf")
    
#     def setColToZero(self, matrix: List[List[int]], col: int):
#         for row in range(len(matrix)):
#             if matrix[row][col] != 0:
#                 matrix[row][col] = float("inf")

    # optimal
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isFirstRowZero = False
        isFirstColZero = False
        
        for col in range(len(matrix[0])):   # check first row for zeroes
            if matrix[0][col] == 0:
                isFirstRowZero = True
                
        for row in range(len(matrix)):  # check first column for zeroes
            if matrix[row][0] == 0:
                isFirstColZero = True
                
        # start from [1][1] index, using first column and row as indicators 
        # for which entire row and columns should have zero
        for row in range(1, len(matrix)):   
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0  # flag first row element
                    matrix[0][col] = 0  # flag first column element
        
        # start at index [1][1], setting all elements to zero as neccessary, 
        # using first row and column indicators
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                # if first row element or first column element is flagged as 0
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if isFirstRowZero:  # set first row to zero if needed
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if isFirstColZero:  # set first column to zero if needed
            for row in range(len(matrix)):
                matrix[row][0] = 0
