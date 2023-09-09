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
    // test cases:
    //                  S        F
    // input: -1->1->2->3->4->5->N n = 2 window = 4
    // output: 1->2->3->5->N
    //
    //         S                 F
    // input: -1->1->2->3->4->5->N n = 5 window = 6
    // output: 2->3->4->5->N
    //
    //                     S     F
    // input: -1->1->2->3->4->5->N n = 1 window = 3
    // output: 1->2->3->4->N
    //
    //         S     F
    // input: -1->2->N n = 1 window = 2
    // output: N
    //
    // optimal sliding window approach
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode *dummyHead = new ListNode(-1, head);
        ListNode *slow = dummyHead, *fast = dummyHead;

        int windowSize = 0;

        while (fast != NULL) {
            fast = fast->next;
            ++windowSize;

            // slow pointer starts moving up once buffer space exceeds n+1 nodes
            if (windowSize > n + 1) {
                slow = slow->next;
            }
        }

        // slow pointer is now right before target to remove
        slow->next = slow->next->next;
        return dummyHead->next;
    }
};
