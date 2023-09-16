/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    // optimal dfs approach
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        // cache isomorphism of original to cloned nodes to attach cycles
        unordered_map<Node *, Node*> clones;
        Node *clonedNode = new Node(node->val);
        cloneSubgraph(node, clonedNode, clones);

        return clonedNode;
    }

    void cloneSubgraph(Node *node, Node *clonedNode, unordered_map<Node*, Node*> &clones) {
        // graph node has already been visited so subgraph from it has already been cloned
        if (clones.find(node) != clones.end()) {
            return;
        }

        // mark current node as visited with the constructed cloned node to
        // lookup and attach if adjacent to another node in graph forming cycle
        clones[node] = clonedNode;

        // clone every child of current graph node and add as child to
        // current cloned node
        for (auto &child : node->neighbors) {
            // if adjacent neighbor by key already visited, it is already cloned
            // and exists in cloned graph so add as child to cloned node to form cycle
            Node *clonedChild = clones.find(child) != clones.end() ?
                clones[child] : new Node(child->val);

            clonedNode->neighbors.push_back(clonedChild);
            cloneSubgraph(child, clonedChild, clones);
        }
    }
};
