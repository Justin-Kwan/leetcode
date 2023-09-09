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
    // optimal recursive approach
    bool isValidBST(TreeNode *root) {
        return this->isValidSubtree(root, LONG_MIN, LONG_MAX);
    }

private:
    bool isValidSubtree(TreeNode *root, long lowerBound, long upperBound) {
        if (root == NULL) {
            return true;
        }
        // subtree is valid if root within range, left subtree falls within
        // tighter upper bound and right subtree should fall within tighter
        // lower bound
        return lowerBound < root->val && root->val < upperBound &&
               this->isValidSubtree(root->left, lowerBound, root->val) &&
               this->isValidSubtree(root->right, root->val, upperBound);
    }
};
