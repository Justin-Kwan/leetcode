class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

# optimal trie dfs approach
class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.trieRoot
        for letter in word:
            child = curNode.children.get(letter)
            if not child:
                child = TrieNode()
                curNode.children[letter] = child
            curNode = child

        curNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.searchExpression(self.trieRoot, word, 0)

    def searchExpression(self, parent: TrieNode, word: str, curPos: int) -> bool:
        if curPos >= len(word):
            return parent.isEndOfWord

        # match on exact same child letter if current word character is letter
        if word[curPos].isalpha():
            curNode = parent.children.get(word[curPos])
            if not curNode:
                return False
            return self.searchExpression(curNode, word, curPos + 1)
 
        # match on any child letter if current word character is '.'
        for curNode in parent.children.values():
            if self.searchExpression(curNode, word, curPos + 1):
                return True
        # exhausted all children to search for a grandchild that matches next
        # letter after sequence of '.' in word or is an end of word node if no
        # letters after sequence of '.'
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
