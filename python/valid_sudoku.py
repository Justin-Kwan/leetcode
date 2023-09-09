import math

class Solution:
    # optimal single pass hashmap approach
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardLength = len(board)

        # use sets to track seen digits for each row, column and submatrix
        seenRowDigits = [set() for _ in range(boardLength)]
        seenColDigits = [set() for _ in range(boardLength)]
        seenSubmatrixDigits = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(boardLength):
            for col in range(boardLength):
                digit = board[row][col]

                if digit == ".":
                    continue

                # check current digit not duplicated in row, column and submatrix of
                # 3 x 3 by hashing row and column positions of 9 x 9 matrix to 3 x 3
                # matrix of sets
                if (digit in seenRowDigits[row] or
                    digit in seenColDigits[col] or
                    digit in seenSubmatrixDigits[row // 3][col // 3]):
                    return False

                # mark digit as seen in current row, column and submatrix
                # (assuming board only contains valid digits from 1-9)
                seenRowDigits[row].add(digit)
                seenColDigits[col].add(digit)
                seenSubmatrixDigits[row // 3][col // 3].add(digit)

        return True

#     # suboptimal triple pass hashmap approach
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         boardLength = len(board)
#         seenDigits = set()

#         # check each row is valid
#         for row in board:
#             for char in row:
#                 # detect invalid digit, or duplicate valid digit
#                 if (char.isdigit() and not self.isValidDigit(char)) or char in seenDigits:
#                     return False

#                 if self.isValidDigit(char):
#                     seenDigits.add(char)

#             seenDigits.clear()

#         # check each column is valid
#         for col in range(boardLength):
#             for row in range(boardLength):
#                 char = board[row][col]

#                 if (char.isdigit() and not self.isValidDigit(char)) or char in seenDigits:
#                     return False

#                 if self.isValidDigit(char):
#                     seenDigits.add(char)

#             seenDigits.clear()

#         # check each submatrix is valid
#         for i in range(0, boardLength * 3, 3):
#             for j in range(0, boardLength * 3, 3):
#                 startRow, startCol = i % boardLength, j % boardLength

#                 for row in range(startRow, startRow + 3):
#                     for col in range(startCol, startCol + 3):
#                         char = board[row][col]

#                         if (char.isdigit() and not self.isValidDigit(char)) or char in seenDigits:
#                             return False

#                         if self.isValidDigit(char):
#                             seenDigits.add(char)

#                 seenDigits.clear()

#         return True

#     def isValidDigit(self, char: str) -> bool:
#         return len(char) == 1 and char.isdigit() and char != "0"