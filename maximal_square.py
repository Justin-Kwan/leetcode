class Solution:
    # optimized DFS with memoization (top down DP)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxSubmatrixLength = 0

        # initialize cache to same size as matrix
        maxLengthCache = [[-1 for col in range(len(matrix[0]))] for row in range(len(matrix))]

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == "1":
                    maxSubmatrixLength = max(maxSubmatrixLength, self.searchMaxSubmatrixLength(row, col, matrix, maxLengthCache))

        return maxSubmatrixLength ** 2

    def searchMaxSubmatrixLength(self, row: int, col: int, matrix: List[List[str]], maxLengthCache: List[List[str]]) -> int:
        if row >= len(matrix) or col >= len(matrix[0]):
            return 0
        if matrix[row][col] == "0":
            maxLengthCache[row][col] = 0
        if maxLengthCache[row][col] != -1:
            return maxLengthCache[row][col]

        # if submatrix length from row, col not in cache, compute it
        maxCurrLength = min(
            self.searchMaxSubmatrixLength(row + 1, col, matrix, maxLengthCache),
            self.searchMaxSubmatrixLength(row, col + 1, matrix, maxLengthCache), 
            self.searchMaxSubmatrixLength(row + 1, col + 1, matrix, maxLengthCache)) + 1

        maxLengthCache[row][col] = maxCurrLength
        return maxCurrLength

#     # unoptimized DFS brute force
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0

#         maxSubmatrixLength = 0
        
#         # for each square of 1, find largest submatrix of 1s starting from it (as left corner)
#         for row in range(0, len(matrix)):
#             for col in range(0, len(matrix[0])):
#                 maxSubmatrixLength = max(self.searchMaxSubmatrixLength(row, col, matrix), maxSubmatrixLength)

#         # return max submatrix's area                
#         return maxSubmatrixLength ** 2

#     def searchMaxSubmatrixLength(self, row: int, col: int, matrix: List[List[str]]) -> int:
#         if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == "0":
#             return 0

#         # minimum of squares from below, right, and diagonal right + 1 makes current length
#         maxCurrLength = min(
#             self.searchMaxSubmatrixLength(row + 1, col, matrix),
#             self.searchMaxSubmatrixLength(row, col + 1, matrix),
#             self.searchMaxSubmatrixLength(row + 1, col + 1, matrix)) + 1

#         # return max length of submatrix of 1s up to current position
#         return maxCurrLength
        

#     # unoptimized BFS brute force
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return

#         largestSubmatrixOfOnesArea = 0

#         # trigger BFS for every square of "1"
#         for row in range(0, len(matrix)):
#             for col in range(0, len(matrix[0])):
#                 if matrix[row][col] == "1":
#                     largestSubmatrixOfOnesArea = max(largestSubmatrixOfOnesArea, self.searchLargestSubmatrixOfOnesArea(row, col, matrix))

#         return largestSubmatrixOfOnesArea

#     def searchLargestSubmatrixOfOnesArea(self, fromRow: int, fromCol: int, matrix: List[List[str]]) -> int:
#         maxAreaSoFar = 0
#         neighborsToVisit = collections.deque([(fromRow, fromCol)])

#         # can use while true...
#         while True:
#             # take snapshot of squares layer count
#             layerCount = len(neighborsToVisit)
#             maxAreaSoFar += layerCount

#             for i in range(0, layerCount):
#                 cellPos = neighborsToVisit.popleft()
#                 row = cellPos[0]
#                 col = cellPos[1]

#                 if row + 1 >= len(matrix) or col + 1 >= len(matrix[0]) or matrix[row + 1][col] == "0" or matrix[row][col + 1] == "0" or matrix[row + 1][col + 1] == "0":
#                     return maxAreaSoFar

#                 # add in neighbors if not already in it
#                 if (row + 1, col) not in neighborsToVisit:
#                     neighborsToVisit.append((row + 1, col))
#                 if (row, col + 1) not in neighborsToVisit:
#                     neighborsToVisit.append((row, col + 1))
#                 if (row + 1, col + 1) not in neighborsToVisit:
#                     neighborsToVisit.append((row + 1, col + 1))
