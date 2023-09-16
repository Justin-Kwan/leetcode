/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // simplified dfs array approach
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> nodesByLevel;
        encodeNodes(root, 0, nodesByLevel);
        return nodesByLevel;
    }

    void encodeNodes(TreeNode *curNode, int curLevel, vector<vector<int>> &nodesByLevel) {
        if (curNode == nullptr) {
            return;
        }

        // observation: any recursive dfs order will always visit all
        // nodes across a level in order

        // extend to store node values at current level upon first time reaching level
        if (nodesByLevel.size() < curLevel + 1) {
            nodesByLevel.push_back({});
        }
        nodesByLevel[curLevel].push_back(curNode->val);

        // collect and write all nodes underneath current level
        encodeNodes(curNode->left, curLevel + 1, nodesByLevel);
        encodeNodes(curNode->right, curLevel + 1, nodesByLevel);
    }

    // // dfs hashmap approach
    // vector<vector<int>> levelOrder(TreeNode *root) {
    //     map<int, vector<int>> nodesByLevel;
    //     encodeNodes(root, 0, nodesByLevel);

    //     vector<vector<int>> answer;
    //     for (auto &[_, nodeLevel] : nodesByLevel) {
    //         answer.push_back(nodeLevel);
    //     }
    //     return answer;
    // }

    // void encodeNodes(TreeNode *curNode, int curLevel, map<int, vector<int>> &nodesByLevel) {
    //     if (curNode == nullptr) {
    //         return;
    //     }

    //     // collect and write all nodes underneath current level first
    //     encodeNodes(curNode->left, curLevel + 1, nodesByLevel);
    //     encodeNodes(curNode->right, curLevel + 1, nodesByLevel);
    //     nodesByLevel[curLevel].push_back(curNode->val);
    // }

    // // bfs approach
    // vector<vector<int>> levelOrder(TreeNode* root) {
    //     if (root == nullptr) {
    //         return {};
    //     }

    //     vector<vector<int>> nodesByLevel;
    //     deque<TreeNode*> nodesToVisit = { root };

    //     while (!nodesToVisit.empty()) {
    //         int totalLevelNodes = nodesToVisit.size();
    //         vector<int> nodeLevel;

    //         // capture and store all node values in current bfs level
    //         for (int _ = 0; _ < totalLevelNodes; ++_) {
    //             TreeNode *curNode = nodesToVisit.front();
    //             nodesToVisit.pop_front();
    //             nodeLevel.push_back(curNode->val);

    //             // do not queue null children to visit in next level
    //             if (curNode->left != nullptr) {
    //                 nodesToVisit.push_back(curNode->left);
    //             }
    //             if (curNode->right != nullptr) {
    //                 nodesToVisit.push_back(curNode->right);
    //             }
    //         }

    //         nodesByLevel.push_back(nodeLevel);
    //     }

    //     return nodesByLevel;
    // }
};
