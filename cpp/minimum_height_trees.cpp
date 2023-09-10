class Solution {
public:
    // suboptimal dfs hashmap approach
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
        // single node with no edges is trivially root of MHT
        if (n == 1) {
            return { 0 };
        }

        unordered_map<int, vector<int>> tree;
        unordered_set<int> visited;

        long minTreeHeight = LONG_MAX;
        vector<int> minHeightRoots;

        // construct hashmap graph of nodes by adjacencies bidirectionally of children 
        // and parent), all nodes must be incident to an edge since tree always connected
        // by definition
        for (auto &edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }

        // search height of tree when each current node is root
        for (int node = 0; node < n; ++node) {
            int curTreeHeight = this->countTreeHeight(tree, visited, node);
            // replace minimum height tree roots if current root obtains shorter tree
            if (curTreeHeight < minTreeHeight) {
                minTreeHeight = curTreeHeight;
                minHeightRoots = { node };
            }
            // add current root if tree of same minimum height obtained
            else if (curTreeHeight == minTreeHeight) {
                minHeightRoots.push_back(node);
            }
        }

        return minHeightRoots;
    }

private:
    int countTreeHeight(unordered_map<int, vector<int>> tree, unordered_set<int> visited, int root) {
        // do not revisit an adjacent node bidirectionally (parent)
        if (visited.find(root) != visited.end()) {
            return 0;
        }
        visited.insert(root);

        // current tree height is 1 + height of tallest subtree
        int maxSubtreeHeight = 0;
        for (auto &child : tree.find(root)->second) {
            int curSubtreeHeight = this->countTreeHeight(tree, visited, child);
            maxSubtreeHeight = max(curSubtreeHeight, maxSubtreeHeight);
        }

        visited.erase(root);
        return 1 + maxSubtreeHeight;
    }
};
