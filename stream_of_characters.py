class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

# optimal multiple pointers (bfs) approach
class StreamChecker:
    def __init__(self, words: List[str]):
        # track all pointers currently searching for a word match given
        # sequence of past characters from stream (stream not saved)
        #
        # using K pointers allows us to search for overlapping or contained
        # word matches within character stream at the same time, instead of
        # a single pointer which would not know whether to abort or continue
        self.searchPointers = collections.deque([])
        self.root = TrieNode()

        # initially construct trie by inserting each given word
        for word in words:
            curNode = self.root

            for nextLetter in word:
                child = curNode.children.get(nextLetter)
                if not child:
                    child = TrieNode()
                    curNode.children[nextLetter] = child
                curNode = child

            # flag last node as last character of word
            curNode.isLast = True

    def query(self, letter: str) -> bool:
        # set idle pointer at root to begin matching a word given next
        # letter in stream (pruned if no word in trie starts with letter)
        self.searchPointers.append(self.root)

        # try advancing all pointers searching for word match given next letter
        totalMatchedWords = 0
        for _ in range(len(self.searchPointers)):
            searchPointer = self.searchPointers.popleft()
            # prune out search pointer if next character not a child since
            # no match exists (pointer cannot advance)
            child = searchPointer.children.get(letter)
            if not child:
                continue

            # next letter in stream completes a word in the trie, if search
            # pointer advances to a "last" node
            if child.isLast:
                totalMatchedWords += 1
            # advance the pointer by replacing it with its child
            self.searchPointers.append(child)

        # letter completes a suffix matching at least one word in trie
        return totalMatchedWords >= 1


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
