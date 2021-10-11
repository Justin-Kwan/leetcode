# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current is not None:
            tempNext = current.next    # store 3
            current.next = prev        # 2 -> 1
            prev = current      # store 2 for reference at node 3
            current = tempNext
        
        return prev

