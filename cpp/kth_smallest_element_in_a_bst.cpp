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
    // iterative inorder traversal approach
    // time complexity:  O(N + k) <= O(2N) => O(N) for N nodes in tree in worst case
    //                   when tree skewed to left branch and kth smallest is any node
    //                   at most N, since visiting all N nodes to the left leaf and
    //                   stack is popped k times until kth smallest node reached
    // space complexity: O(N) for N nodes in tree in worst case when tree is skewed
    //                   on left branch and kth smallest is any node (since must dfs
    //                   to left leaf first) where stack grows to store N nodes
    //                   (stack will only ever contain one node with right skewed tree)
    int kthSmallest(TreeNode* root, int k) {
        if (root == nullptr) {
            return -1;
        }

        stack<TreeNode*> nodeStack({ root });
        TreeNode * kthNode;

        while (!nodeStack.empty()) {
            // keep recursing on left child of current node
            while (root != nullptr) {
                nodeStack.push(root);
                root = root->left;
            }
            // base case reached null left or right child node, return back to
            // parent node if recursed on left child, or return to previous
            // parent above subtree if recursed on right child
            root = nodeStack.top();
            nodeStack.pop();

            // decrement k nodes while backtracking during inorder traversal,
            // return value at kth smallest node once found
            --k;
            if (k == 0) {
                kthNode = root;
                break;
            }
            // recurse on right child of current node, then return to previous
            // parent to complete left current right traversal order
            root = root->right;
        }

        return kthNode->val;
    }

    // // recursive inorder traversal counter approach
    // // time complexity:  O(N) for N nodes in worst case where kth smallest node
    // //                   is smallest or largest (k = 1 or k = N) in left or right 
    // //                   skewed tree so all N nodes must be visited
    // //                   O(K) for kth smallest node value to find on average by
    // //                   preventing further recursive dfs once kth smallest found
    // // space complexity: O(N) for N nodes in worst case where tree is skewed to
    // //                   left branch and kth smallest is any node (since must always
    // //                   dfs to left leaf first) or tree is skewed to right branch
    // //                   and kth smallest is largest node (k = N), both requiring 
    // //                   call stack depth of N
    // int kthSmallest(TreeNode* root, int k) {
    //     TreeNode *kthNode;
    //     kthSmallestNode(root, make_unique<int>(k), kthNode);
    //     return kthNode->val;
    // }

    // void kthSmallestNode(TreeNode *curNode, const unique_ptr<int> &k, TreeNode *&kthNode) {
    //     // reached the leftmost leaf which is the smallest node
    //     if (curNode == nullptr) {
    //         return;
    //     }

    //     kthSmallestNode(curNode->left, k, kthNode);

    //     // decrement k nodes while backtracking during inorder traversal
    //     // (counter decrements when backtracking left branch from smaller
    //     // to larger nodes, or recursing on right branch from smaller to
    //     // larger)
    //     --(*k);
    //     // stop dfs searching if kth smallest already found, otherwise if
    //     // current node is kth smallest, assign return pointer to it
    //     if (*k < 0) {
    //         return;
    //     }
    //     else if (*k == 0) {
    //         kthNode = curNode;
    //         return;
    //     }

    //     kthSmallestNode(curNode->right, k, kthNode);
    // }
};
