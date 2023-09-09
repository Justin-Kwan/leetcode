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
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        // keep searching for cycle until linked list terminates
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            // cycle is found so stop searching
            if (slow == fast) {
                break;
            }
        }

        // linked list has no cycle if it terminated at null tail
        if (fast == NULL || fast->next == NULL) {
            return NULL;
        }

        // search for first node in cycle which is always same distance
        // away from "collision" node as from list head
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return fast;
    }
};
