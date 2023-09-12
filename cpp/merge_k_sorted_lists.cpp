/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // optimal recursive merge sort approach
    ListNode *mergeKLists(vector<ListNode*> &lists) {
        if (lists.empty()) {
            return nullptr;
        }
        return mergeLists(lists, 0, lists.size() - 1);
    }

    ListNode *mergeLists(vector<ListNode*> &lists, int start, int end) {
        // return single list of nodes to be merged after splitting 
        if (start == end) {
            return lists[start];
        }

        // partition to get partially merged left and right linked lists nodes from
        // subtrees and merge here
        int middle = (start + end) / 2;
        ListNode *leftMergedNodes = mergeLists(lists, start, middle);
        ListNode *rightMergedNodes = mergeLists(lists, middle + 1, end);

        return mergeTwoLists(leftMergedNodes, rightMergedNodes);
    }

    ListNode *mergeTwoLists(ListNode *list, ListNode *other) {
        if (list == nullptr && other == nullptr) {
            return nullptr;
        }

        ListNode *dummyHead = new ListNode(-1);
        ListNode *curNode = dummyHead;

        // keep merging while both lists still have nodes (one will exhaust first)
        while (list != nullptr && other != nullptr) {
            if (list->val < other->val) {
                curNode->next = list;
                list = list->next;
            } else {
                curNode->next = other;
                other = other->next;
            }
            curNode = curNode->next;
        }
        // add rest of a list's nodes to merged list once other is exhaused
        // since they're larger (always case that one list exhausts with other
        // containing one or more nodes left)
        curNode->next = (other == nullptr) ? list : other;
        return dummyHead->next;
    }
};
