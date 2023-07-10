# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # optimal merge heads approach
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curHead = mergedHead = ListNode(-1)

        # keep merging while both lists still have nodes
        while list1 and list2:
            if list1.val < list2.val:
                curHead.next = list1
                list1 = list1.next
            else:
                curHead.next = list2
                list2 = list2.next

            curHead = curHead.next

        # add rest of a list's nodes to merged list once other is exhausted
        # since they're larger (usual case of one node left in one list)
        curHead.next = list2 if not list1 else list1

        return mergedHead.next

# test cases:

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: l1 = [1,2,4,5,6], l2 = [1,3,4]
# Output: [1,1,2,3,4,4,5,6]

# Input: l1 = [1,3,4], l2 = [1,2,4,5,6]
# Output: [1,1,2,3,4,4,5,6]

# Input: l1 = [1, 1], l2 = [1, 1]
# Output: [1,1,1,1]

# Input: l1 = [1, 1, 1, 1], l2 = [50]
# Output: [1, 1, 1, 1, 50]

# Input: l1 = [2], l2 = [1]
# Output: [1, 2]
