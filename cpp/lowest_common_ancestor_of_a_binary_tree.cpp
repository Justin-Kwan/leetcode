/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    TreeNode *lcaNode = nullptr;

public:
    // optimal simplified recursive dfs approach
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        containsPq(root, p, q);
        return lcaNode;
    }

    bool containsPq(TreeNode *curNode, TreeNode* p, TreeNode* q) {
        if (curNode == nullptr) {
            return false;
        }

        // current node is LCA if (wlog) root is p and q in left or right subtree,
        // or p is in left subtree and q is in right subtree
        bool isPqRoot = curNode->val == p->val or curNode->val == q->val;
        bool isPqInLeft = containsPq(curNode->left, p, q);
        bool isPqInRight = containsPq(curNode->right, p, q);

        // two of three conditions must be true at LCA for unique p and q since node
        // values are unique (only pq in left or pq in right are true above LCA node)
        if ((isPqRoot && isPqInLeft) || (isPqRoot && isPqInRight) || (isPqInLeft && isPqInRight))
        {
            lcaNode = curNode;
        }
        // report whether p or q in current subtree for parent to check if LCA
        return isPqRoot || isPqInLeft || isPqInRight;
    }

    // // optimal recursive dfs approach
    // TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    //     searchLcaNode(root, p, q);
    //     return lcaNode;
    // }

    // pair<bool, bool> searchLcaNode(TreeNode *curNode, TreeNode* p, TreeNode* q) {
    //     if (curNode == nullptr) {
    //         return make_pair(false, false);
    //     }

    //     auto [isPInLeft, isQInLeft] = searchLcaNode(curNode->left, p, q);
    //     auto [isPInRight, isQInRight] = searchLcaNode(curNode->right, p, q);

    //     // current node is LCA if (wlog) root is p and q in left or right subtree,
    //     // or p is in left subtree and q is in right subtree
    //     if ((curNode->val == p->val && (isQInLeft || isQInRight)) or
    //         (curNode->val == q->val && (isPInLeft || isPInRight)) ||
    //         (isPInLeft && isQInRight) || (isQInLeft && isPInRight))
    //     {
    //         lcaNode = curNode;
    //     }
    //     // report whether p and q in current subtree for parent to check if LCA
    //     return make_pair(
    //         isPInLeft || isPInRight || curNode->val == p->val,
    //         isQInLeft || isQInRight || curNode->val == q->val
    //     );
    // }

    // // optimal iterative dfs approach
    // TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    //     if (root == nullptr) {
    //         return root;
    //     }

    //     unordered_map<TreeNode*, TreeNode*> nodeParents{{ root, nullptr }};
    //     stack<TreeNode*> stack({ root });

    //     // keep traversing nodes until both p and q visited and added to parents
    //     while (nodeParents.find(p) == nodeParents.end() || nodeParents.find(q) == nodeParents.end()) {
    //         TreeNode* curNode = stack.top(); stack.pop();
    //         // push right child on stack so to visit left subtree first following
    //         // preorder traversal (all lefts visited first then rights), save each
    //         // child's parent in order to backtrack
    //         if (curNode->right != nullptr) {
    //             stack.push(curNode->right);
    //             nodeParents[curNode->right] = curNode;
    //         }
    //         if (curNode->left != nullptr) {
    //             stack.push(curNode->left);
    //             nodeParents[curNode->left] = curNode;
    //         }
    //     }

    //     unordered_set<TreeNode*> ancestors;

    //     // add all ancestors of p to set (all the way back to root) while each parent exists
    //     while (p != nullptr) {
    //         ancestors.insert(p);
    //         p = nodeParents[p];
    //     }
    //     // then go through q's ancestors and find first common one with p
    //     while (ancestors.find(q) == ancestors.end()) {
    //         q = nodeParents[q];
    //     }
    //     return q;
    // }
};
