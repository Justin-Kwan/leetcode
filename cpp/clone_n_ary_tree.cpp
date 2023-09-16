/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    // bfs approach
    // time complexity:  O(N) snce visiting all N nodes by queueing each node by
    //                   queueing and dequeueing to visit its children until all
    //                   nodes visited and cloned
    // space complexity: O(N-1) => O(N) worst case that all N-1 nodes are children
    //                   of root node so queue grows to size N-1, in general case,
    //                   number of nodes in queue always bounded by N
    Node* cloneTree(Node *root) {
        if (root == nullptr) {
            return nullptr;
        }

        Node *rootClone = new Node(root->val);
        deque<pair<Node*, Node*>> nodesToVisit = { make_pair(root, rootClone) };

        while(!nodesToVisit.empty()) {
            auto [node, nodeClone] = nodesToVisit.front();
            nodesToVisit.pop_front();

            // clone children of current node and add to cloned node, then queue them
            for (Node *child : node->children) {
                Node *childClone = new Node(child->val);
                nodeClone->children.push_back(childClone);
                nodesToVisit.push_back(make_pair(child, childClone));
            }
        }

        return rootClone;
    }

    // // dfs approach
    // // time complexity:  O(N) since visiting all N nodes in original tree to clone
    // // space complexity: O(2N) => O(N) for worst case all N n-ary nodes are skewed
    // //                   forming a single branch of all nodes resulting in recursive
    // //                   call stack depth of N
    // Node* cloneTree(Node *root) {
    //     if (root == nullptr) {
    //         return nullptr;
    //     }

    //     Node *rootClone = new Node(root->val);
    //     for (Node *child : root->children) {
    //         Node *childClone = cloneTree(child);
    //         rootClone->children.push_back(childClone);
    //     }

    //     return rootClone;
    // }
};
