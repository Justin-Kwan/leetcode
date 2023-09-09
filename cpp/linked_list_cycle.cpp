/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // optimal floyd's algorithm approach
    bool hasCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        // keep searching for cycle until link list terminates
        while (fast != NULL && fast->next != NULL) {
            // move slow and fast pointers first to avoid detecting
            // cycle when both are at list head
            slow = slow->next;
            fast = fast->next->next;

            // cycle exists if fast pointer laps and reaches slow pointer
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
};
