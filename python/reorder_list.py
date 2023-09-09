# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     # suboptimal triple pass approach
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head:
#             return None

#         # count list's length to know middle position to start reversing from
#         listLength = 0
#         tempHead = head

#         while tempHead:
#             listLength += 1
#             tempHead = tempHead.next

#         # reverse second half of list to access previous nodes before tail
#         tempHead = head # first node before reversed nodes
#         middlePos = (listLength // 2) - 1 if (listLength % 2 == 0) else (listLength // 2)

#         for _ in range(middlePos):
#             tempHead = tempHead.next

#         # must break off reversed list from original in order to merge it back
#         tempTail = self.reverseList(tempHead.next)
#         tempHead.next = None
#         tempHead = head

#         # place nodes starting from tail in-between nodes starting from head
#         while tempTail:
#             # attach current tail inbetween head and head's next node
#             nextHead = tempHead.next
#             tempHead.next = tempTail

#             # attach current head inbetween tail and tail's next node
#             nextTail = tempTail.next
#             tempTail.next = nextHead

#             tempHead = nextHead
#             tempTail = nextTail

#         return head

    # optimal double pass approach
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # find middle node before first node to be reversed in second half of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse tail end of list, must break off from original in order to merge it back
        tempTail = self.reverseList(slow.next)
        slow.next = None

        # interweave reversed tail half of list to first half
        tempHead = head
        while tempTail:
            # attach current tail inbetween head and head's next node
            nextHead = tempHead.next
            tempHead.next = tempTail

            # attach current head inbetween tail and tail's next node
            nextTail = tempTail.next
            tempTail.next = nextHead

            # traverse to next head and tail nodes (one away from current)
            tempHead, tempTail = nextHead, nextTail

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNext = None
        tempPrev = None

        while head:
            tempNext = head.next
            head.next = tempPrev

            tempPrev = head
            head = tempNext

        return tempPrev
