struct TrieNode {
private:
    TrieNode *children[26];

public:
    bool isEndOfWord;

    TrieNode() : isEndOfWord{false} {
        fill_n(children, 26, nullptr);
    }

    TrieNode *findChild(char letter) {
        return children[letter - 'a'];
    }

    TrieNode *addChild(char letter) {
        TrieNode *child = new TrieNode();
        children[letter - 'a'] = child;
        return child;
    }
};

// optimal iterative approach
class Trie {
private:
    TrieNode *root;

public:
    Trie() : root{new TrieNode()} {
    }

    void insert(string word) {
        TrieNode *curNode = root;

        for (char letter : word) {
            // lookup next character child node, create and add if not exists
            TrieNode *child = curNode->findChild(letter);
            if (child == nullptr) {
                child = curNode->addChild(letter);
            }
            curNode = child;
        }
        // mark last character node as last in word path
        curNode->isEndOfWord = true;
    }

    bool search(string word) {
        // make sure current node is the end of a word, otherwise current nodes
        // are only a prefix of a longer word in trie
        TrieNode *letterNode = searchPath(word);
        return letterNode != nullptr && letterNode->isEndOfWord;
    }

    bool startsWith(string prefix) {
        // any word in trie is always a prefix of itself
        TrieNode *letterNode = searchPath(prefix);
        return letterNode != nullptr;
    }

    TrieNode *searchPath(string word) {
        TrieNode *curNode = root;

        for (char letter : word) {
            TrieNode *child = curNode->findChild(letter);
            if (child == nullptr) {
                return nullptr;
            }
            curNode = child;
        }
        // word is either in trie or a prefix of another word in trie
        return curNode;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
