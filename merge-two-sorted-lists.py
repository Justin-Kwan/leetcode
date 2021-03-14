# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # optimal
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        currNode1 = l1
        currNode2 = l2

        dummyHead = ListNode(0, None)
        dummyHeadRef = dummyHead
        
        while currNode1 is not None and currNode2 is not None:

            if currNode1.val < currNode2.val:
                dummyHead.next = currNode1
                currNode1 = currNode1.next
            else:
                dummyHead.next = currNode2
                currNode2 = currNode2.next

            dummyHead = dummyHead.next
        
        # at this point, at least one node is null
        if currNode1 is None:
            dummyHead.next = currNode2
        if currNode2 is None:
            dummyHead.next = currNode1

        return dummyHeadRef.next

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
