class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    # optimal dfs trie pruning approach
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct trie of words to guide faster dfs for word matches
        trieRoot = TrieNode()
        for word in words:
            curNode = trieRoot

            for letter in word:
                child = curNode.children.get(letter)
                if not child:
                    child = TrieNode()
                    curNode.children[letter] = child
                curNode = child

            curNode.isEndOfWord = True

        # dfs for any word matches starting at each board letter
        foundWords = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.searchBoardWords(board, (row, col), trieRoot, [], foundWords)

        return foundWords

    def searchBoardWords(self, board: List[List[str]], cell: tuple[int, int], parent: TrieNode, curWord: List[str], foundWords: set[str]) -> None:
        # cell out of bounds, already visited or its letter not in trie path
        row, col = cell
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or
            not board[row][col].isalpha() or board[row][col] not in parent.children):
            return

        # letter in trie path, mark it as visited and append to current word
        cellLetter, board[row][col] = board[row][col], '#'
        curWord.append(cellLetter)

        # append current word and continue searching for longer words
        curNode = parent.children[cellLetter]
        if curNode.isEndOfWord:
            foundWords.add("".join(curWord))

        for rowMove, colMove in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nextCell = (row + rowMove, col + colMove)
            self.searchBoardWords(board, nextCell, curNode, curWord, foundWords)

        # restore current cell as unvisited
        board[row][col] = cellLetter
        curWord.pop()

        # optimize by pruning matched word path to avoid searching it again
        # (only if no other words are shared by path)
        if not curNode.children:
            parent.children.pop(cellLetter)
