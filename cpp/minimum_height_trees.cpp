class Solution {
public:
    // optimal topological sort approach
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
        // single node with no edges is trivially root of MHT
        if (n == 1) {
            return { 0 };
        }

        // trim leaf nodes and edges without modifying original graph
        vector<int> degreesByNode(n, 0);
        unordered_map<int, vector<int>> tree;

        // construct hashmap undirected graph of nodes by adjacencies where each node contains
        // its children and parent, count the number of total edges for each node
        for (auto &edge : edges) {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
            ++degreesByNode[edge[0]];
            ++degreesByNode[edge[1]];
        }

        // queue leaves of tree as initial layer of nodes to trim
        queue<int> leavesToTrim;
        for (auto &[node, children] : tree) {
            // node is a leaf if it's only adjacent to its parent
            if (children.size() == 1) {
                leavesToTrim.push(node);
            }
        }

        // trim layer by layer of leaf nodes in tree, last layer of nodes captured are centroids
        vector<int> centroids;
        while (!leavesToTrim.empty()) {
            int totalLeaves = leavesToTrim.size();
            centroids.clear();

            // trim current layer of leaf nodes from tree
            for (int _ = 0; _ < totalLeaves; ++_) {
                int curLeaf = leavesToTrim.front(); leavesToTrim.pop();
                centroids.push_back(curLeaf);

                //  trim leaf and edge by decrementing degrees of itself and parent
                for (auto &parent : tree[curLeaf]) {
                    --degreesByNode[curLeaf];
                    --degreesByNode[parent];

                    // queue parent node to trim upon becoming a leaf the first time
                    if (degreesByNode[parent] == 1) {
                        leavesToTrim.push(parent);
                    }
                }
            }
        }

        // last layer of leaves trimmed are the centroid roots for MHTs
        return centroids;
    }

// public:
//     // suboptimal dfs hashmap approach
//     vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
//         // single node with no edges is trivially root of MHT
//         if (n == 1) {
//             return { 0 };
//         }

//         unordered_map<int, vector<int>> tree;
//         unordered_set<int> visited;

//         long minTreeHeight = LONG_MAX;
//         vector<int> minHeightRoots;

//         // construct hashmap undirected graph of nodes by adjacencies where each node contains
//         // its children and parent, count the number of total edges for each node
//         for (auto &edge : edges) {
//             tree[edge[0]].push_back(edge[1]);
//             tree[edge[1]].push_back(edge[0]);
//         }

//         // search height of tree when each current node is root
//         for (int node = 0; node < n; ++node) {
//             int curTreeHeight = this->countTreeHeight(tree, visited, node);
//             // replace minimum height tree roots if current root obtains shorter tree
//             if (curTreeHeight < minTreeHeight) {
//                 minTreeHeight = curTreeHeight;
//                 minHeightRoots = { node };
//             }
//             // add current root if tree of same minimum height obtained
//             else if (curTreeHeight == minTreeHeight) {
//                 minHeightRoots.push_back(node);
//             }
//         }

//         return minHeightRoots;
//     }

// private:
//     int countTreeHeight(unordered_map<int, vector<int>> tree, unordered_set<int> visited, int root) {
//         // do not revisit an adjacent node bidirectionally (parent)
//         if (visited.find(root) != visited.end()) {
//             return 0;
//         }
//         visited.insert(root);

//         // current tree height is 1 + height of tallest subtree
//         int maxSubtreeHeight = 0;
//         for (auto &child : tree.find(root)->second) {
//             int curSubtreeHeight = this->countTreeHeight(tree, visited, child);
//             maxSubtreeHeight = max(curSubtreeHeight, maxSubtreeHeight);
//         }

//         visited.erase(root);
//         return 1 + maxSubtreeHeight;
//     }
};
