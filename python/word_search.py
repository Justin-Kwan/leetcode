class Solution:
    # optimal dfs approach
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isWordFound(row: int, col: int, wordPos: int) -> bool:
            # reached end of word, all letters matched
            if wordPos >= len(word):
                return True

            # went out of range of board or cell does not match letter
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or
                board[row][col] != word[wordPos]):
                return False

            # mark current matching cell as visited in current dfs path
            board[row][col] = "#"

            # since current board cell matches character, check remaining
            # characters are found in any neighboring paths
            exists = (isWordFound(row + 1, col, wordPos + 1) or
                      isWordFound(row - 1, col, wordPos + 1) or
                      isWordFound(row, col + 1, wordPos + 1) or
                      isWordFound(row, col - 1, wordPos + 1))

            # restore cell with letter to revisit from another dfs path
            board[row][col] = word[wordPos]
            return exists

        for row in range(len(board)):
            for col in range(len(board[row])):
                # avoid triggering dfs word match on every cell
                if board[row][col] == word[0] and isWordFound(row, col, 0):
                        return True

        # word not found after exhaustively searching entire board
        return False
