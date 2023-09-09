# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # # non optimal
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     listLen = 0
    #     tempHead = head
    #     while tempHead is not None:
    #         listLen += 1
    #         tempHead = tempHead.next
    #     tempHead = head
    #     if n == listLen:    # if first node is to be removed
    #         return head.next
    #     for i in range(listLen - n - 1): # go to node right before one to remove
    #         tempHead = tempHead.next
    #     tempHead.next = tempHead.next.next
    #     return head
    
    # # single pass with hash map
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     nodeMap = {}
    #     listLen = 1
    #     tempHead = head
    #     while tempHead is not None: # put all nodes in hash map
    #         nodeMap[listLen] = tempHead
    #         tempHead = tempHead.next
    #         listLen += 1
    #     if n == listLen - 1:    # if first node to be removed
    #         return head.next
    #     # remove next node by referencing hash map element of node before
    #     nodeMap[listLen - n - 1].next = nodeMap[listLen - n - 1].next.next
    #     return head
    
    # two pointers (optimal)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fastPtr = head
        slowPtr = head
        for i in range(n): # move fast pointer n away from first node
            fastPtr = fastPtr.next
        if fastPtr == None: # if first node should be removed
            return head.next
        # move fast pointer and slow pointer at same pace keeping gap between them
        while fastPtr.next is not None: 
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        slowPtr.next = slowPtr.next.next
        return head

    # optimized
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        headPtr = ListNode(0, head)
        tailPtr = headPtr
        headRef = headPtr
        
        headBufferCount = 0

        while headPtr is not None:
            headPtr = headPtr.next
            headBufferCount += 1
            
            # at least gap of two hops (min case) plus n
            if headBufferCount >= n + 2:
                tailPtr = tailPtr.next
        
        # tailPtr is now right before target node to remove
        tailPtr.next = tailPtr.next.next
        
        # cannot return head, since head could be removed
        return headRef.next

    # cases
    # first node (n = sz)
    # last node (n = 1)
    # 1 node list (n = 1) removing only node in list
    # 2 node list (n = 2) removing first node in list
