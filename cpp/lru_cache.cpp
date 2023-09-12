// optimal doubly linkedlist approach
struct LinkedNode {
    int key, value;
    LinkedNode *prev, *next;

    LinkedNode(int key, int value) : key(key), value(value), prev(nullptr), next(nullptr) {
    }
};

void pushFront(LinkedNode *dummyHead, LinkedNode *node) {
    assert(dummyHead != nullptr);
    assert(node != nullptr);

    // new head node should point to dummy head and next node after
    node->prev = dummyHead;
    node->next = dummyHead->next;
    // dummy head and node after dummy head should point to new head node
    dummyHead->next->prev = node;
    dummyHead->next = node;
}

void unlinkNode(LinkedNode *node) {
    assert(node != nullptr);

    // unlinking is simple since dummy head and tail always on both ends
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

class LRUCache {
private:
    const int capacity;
    unordered_map<int, LinkedNode*> keyValues;

    // keep dummy head in front of MRU key node and dummy tail behind LRU key node
    // to simplify node unlinking annd pushing new node as head
    LinkedNode *mruDummyHead = new LinkedNode(-1, -1);
    LinkedNode *lruDummyTail = new LinkedNode(-1, -1);

public:
    LRUCache(int capacity) : capacity(capacity) {
        this->mruDummyHead->next = this->lruDummyTail;
        this->lruDummyTail->prev = this->mruDummyHead;
    }

    int get(int key) {
        if (keyValues.find(key) == this->keyValues.end()) {
            return -1;
        }

        // move current key node to head since it is the most recently accessed
        LinkedNode *keyNode = this->keyValues[key];
        unlinkNode(keyNode);
        pushFront(this->mruDummyHead, keyNode);

        return keyNode->value;
    }

    void put(int key, int value) {
        LinkedNode *keyNode;

        // update value at key if already exists and unlink its node from list
        if (this->keyValues.find(key) != this->keyValues.end()) {
            keyNode = this->keyValues[key];
            keyNode->value = value;
            unlinkNode(keyNode);
        }
        // otherwise insert key by node containing key and value
        else {
            keyNode = new LinkedNode(key, value);
            this->keyValues[key] = keyNode;
        }

        // move current key node to head since it is the most recently accessed
        pushFront(this->mruDummyHead, keyNode);

        // evict least recently accessed key node at tail when capacity reached
        if (this->keyValues.size() > this->capacity) {
            this->keyValues.erase(this->lruDummyTail->prev->key);
            unlinkNode(this->lruDummyTail->prev);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
