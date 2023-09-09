class TrieNode:
    def __init__(self):
        self._children = [None] * 26
        self.isLast = False

    def addChild(self, child: 'TrieNode', value: str) -> None:
        childPos = self._childPos(value)
        if not self._children[childPos]:
            self._children[childPos] = child

    def getChild(self, value: str) -> Optional['TrieNode']:
        return self._children[self._childPos(value)]

    def _childPos(self, value: str) -> int:
        if len(value) > 1 or (value and not value.isalpha()):
            raise Exception("trie node value must be a letter")
        return ord(value) - ord('a')

# optimal iterative approach
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for nextChar in word:
            # lookup next character child node, create and add if not exists
            child = curNode.getChild(nextChar)
            if not child:
                child = TrieNode()
                curNode.addChild(child, nextChar)
            curNode = child

        # mark last character node as last in word path
        curNode.isLast = True

    def search(self, word: str) -> bool:
        charNode = self.searchPath(word)
        return charNode and charNode.isLast

    def startsWith(self, prefix: str) -> bool:
        # any word in trie is always a prefix of itself
        charNode = self.searchPath(prefix)
        return charNode != None

    def searchPath(self, word: str) -> Optional[TrieNode]:
        curNode = self.root
        for nextChar in word:
            # word not in trie and not prefix if next character not in trie
            child = curNode.getChild(nextChar)
            if not child:
                return None
            curNode = child

        # word is either in trie or a prefix of another
        return curNode


# # recursive approach
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         self.insertWord(self.root, word, 0)

#     def insertWord(self, curNode: TrieNode, word: str, nextPos: int) -> None:
#         # all characters in word have been inserted or already exist as nodes,
#         # flag current node as last character of word
#         if nextPos >= len(word):
#             curNode.isLast = True
#             return

#         # lookup next character as child of current node, create and add to
#         # current node if does not exist
#         child = curNode.getChild(word[nextPos])
#         if not child:
#             child = TrieNode()
#             curNode.addChild(child, word[nextPos])

#         self.insertWord(child, word, nextPos + 1)

#     def search(self, word: str) -> bool:
#         charNode = self.searchPath(self.root, word, 0)
#         return charNode != None and charNode.isLast

#     def startsWith(self, prefix: str) -> bool:
#         # any word in trie is always a prefix of itself
#         charNode = self.searchPath(self.root, prefix, 0)
#         return charNode != None

#     def searchPath(self, curNode: TrieNode, word: str, nextPos: int) -> Optional[TrieNode]:
#         # all word characters are in trie, check if word ends here or is prefix
#         if nextPos >= len(word):
#             return curNode

#         # word not in trie if next character not child of current node
#         child = curNode.getChild(word[nextPos])
#         if not child:
#             return None

#         return self.searchPath(child, word, nextPos + 1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
