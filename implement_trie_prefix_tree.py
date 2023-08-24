from enum import Enum

class SearchResult(Enum):
    WORD = 1
    PREFIX = 2
    MISSING = 3

class TrieNode:
    def __init__(self, value: str = ""):
        self._verifyValue(value)
        self._value = value
        self._children = [None] * 26
        self.isLast = False

    def addChild(self, child) -> None:
        childPos = ord(child._value) - ord('a')
        if not self._children[childPos]:
            self._children[childPos] = child

    def getChild(self, value: str):
        self._verifyValue(value)
        return self._children[ord(value) - ord('a')]

    def _verifyValue(self, value: str) -> None:
        if len(value) > 1 or (value and not value.isalpha()):
            raise Exception("trie node value must be a letter")

# recursive approach
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.insertWord(self.root, word, 0)

    def insertWord(self, curNode: TrieNode, word: str, curPos: int) -> None:
        # all characters in word have been inserted or already exist as nodes,
        # flag current node as last character of word
        if curPos >= len(word):
            curNode.isLast = True
            return

        # lookup next character as child of current node, create and add to
        # current node if does not exist
        child = curNode.getChild(word[curPos])
        if not child:
            child = TrieNode(word[curPos])
            curNode.addChild(child)

        self.insertWord(child, word, curPos + 1)

    def search(self, word: str) -> bool:
        return self.searchWord(self.root, word, 0) == SearchResult.WORD

    def startsWith(self, prefix: str) -> bool:
        search = self.searchWord(self.root, prefix, 0)
        # any word in trie is definitely a prefix
        return search == SearchResult.PREFIX or search == SearchResult.WORD

    def searchWord(self, curNode: TrieNode, word: str, curPos: int) -> SearchResult:
        # all word characters are in trie, check if word ends here or is prefix
        if curPos >= len(word):
            return SearchResult.WORD if curNode.isLast else SearchResult.PREFIX

        # word not in trie if next character not child of current node
        child = curNode.getChild(word[curPos])
        if not child:
            return SearchResult.MISSING

        return self.searchWord(child, word, curPos + 1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
