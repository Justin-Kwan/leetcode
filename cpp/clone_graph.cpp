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
    // optimal bfs hashmap approach
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        Node *nodeClone = new Node(node->val);
        unordered_map<Node*, Node*> clones = {{ node, nodeClone }};
        deque<pair<Node*, Node*>> nodesToVisit = { make_pair(node, nodeClone) };

        while (!nodesToVisit.empty()) {
            auto [node, nodeClone] = nodesToVisit.front();
            nodesToVisit.pop_front();

            // clone children of current graph node and add to cloned node
            for (auto &child : node->neighbors) {
                // adjacent neighbor has already been visited so attach nieghbor clone 
                // to clone node to form cycle, do not revisit this neighbor
                if (clones.find(child) != clones.end()) {
                    nodeClone->neighbors.push_back(clones[child]);
                    continue;
                }

                // otherwise clone neighbor and add to clone node if not visited
                Node *childClone = new Node(child->val);
                nodeClone->neighbors.push_back(childClone);

                // prevent queueing node adjacent to multiple nodes in same layer
                // by marking as visited upon when first queued
                clones[child] = childClone;
                nodesToVisit.push_back(make_pair(child, childClone));
            }
        }

        return nodeClone;
    }

    // // optimal dfs hashmap approach
    // Node* cloneGraph(Node* node) {
    //     if (node == nullptr) {
    //         return nullptr;
    //     }

    //     // cache isomorphism of original to cloned nodes to attach cycles
    //     unordered_map<Node *, Node*> clones;
    //     Node *nodeClone = new Node(node->val);
    //     cloneSubgraph(node, nodeClone, clones);

    //     return nodeClone;
    // }

    // void cloneSubgraph(Node *node, Node *nodeClone, unordered_map<Node*, Node*> &clones) {
    //     // graph node has already been visited so subgraph from it has already been cloned
    //     if (clones.find(node) != clones.end()) {
    //         return;
    //     }

    //     // mark current node as visited with the constructed cloned node
    //     clones[node] = nodeClone;

    //     // clone children of current graph node and add to cloned node
    //     for (auto &child : node->neighbors) {
    //         // adjacent neighbor has already been visited so attach nieghbor clone 
    //         // to clone node to form cycle, do not revisit this neighbor
    //         Node *childClone = clones.find(child) != clones.end() ?
    //             clones[child] : new Node(child->val);

    //         nodeClone->neighbors.push_back(childClone);
    //         cloneSubgraph(child, childClone, clones);
    //     }
    // }
};
