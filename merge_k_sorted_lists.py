# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # optimal min heap approach
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # order current layer of list heads to compare and find minimum
        sortedNodeLayer = []

        # load first layer of linked list heads into min heap to reach all
        # nodes in all lists (node value by index of list it's head of)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(sortedNodeLayer, (lists[i].val, i))

        # merged linked list pointer starts at dummy head
        mergedHead = curHead = ListNode(-1)

        # keep comparing nodes in layer and adding their next ones until all
        # list of nodes are exhausted
        while sortedNodeLayer:
            # pop next minimum node in current layer of comparison
            _, nodeListPos = heapq.heappop(sortedNodeLayer)
            minLayerNode = lists[nodeListPos]

            if minLayerNode.next:
                heapq.heappush(sortedNodeLayer, (minLayerNode.next.val, nodeListPos))
                # make minimum's next node the head of list at index, used once
                # popped later
                lists[nodeListPos] = minLayerNode.next

            curHead.next = minLayerNode
            curHead = curHead.next

        curHead.next = None
        return mergedHead.next
